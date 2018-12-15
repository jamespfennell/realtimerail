import csv
import os
import importlib
import yaml

from transiter.data import database
from transiter.data.dams import systemdam
from transiter.services.update import gtfsstaticutil
from transiter.general import linksutil
from transiter.services.servicepattern import servicepatternmanager
from . import exceptions
from transiter import models


@database.unit_of_work
def list_all():
    """
    List all installed systems.
    :return: A list of short representation of systems
    """
    response = []
    for system in systemdam.list_all():
        system_response = system.short_repr()
        print(system_response)
        system_response.update({
            'href': linksutil.SystemEntityLink(system)
        })
        response.append(system_response)
    return response


@database.unit_of_work
def get_by_id(system_id):
    system = systemdam.get_by_id(system_id)
    if system is None:
        raise exceptions.IdNotFoundError
    response = system.short_repr()
    response.update({
        "stops": {
            "count": systemdam.count_stops_in_system(system_id),
            "href": linksutil.StopsInSystemIndexLink(system)
        },
        "routes": {
            "count": systemdam.count_routes_in_system(system_id),
            "href": linksutil.RoutesInSystemIndexLink(system)
        },
        "feeds": {
            "count": systemdam.count_feeds_in_system(system_id),
            "href": linksutil.FeedsInSystemIndexLink(system)
        }
    })
    return response


@database.unit_of_work
def install(system_id, package='transiter_nycsubway'):
    if systemdam.get_by_id(system_id) is not None:
        return False

    system = systemdam.create()
    system.id = system_id
    system.package = package

    _import_static_data(system)
    return True


@database.unit_of_work
def delete_by_id(system_id):

    """
    print(time.time())
    print('Routes')
    for route in system.routes:
        session.delete(route)
    session.commit()
    print(time.time())
    print('Stops')
    for stop in system.stations:
        session.delete(stop)
    session.commit()
    print(time.time())
    print('Rest')
    #session.delete(system)

    return True
    """

    deleted = systemdam.delete_by_id(system_id)
    if not deleted:
        raise exceptions.IdNotFoundError
    return True


def _lift_stop_properties(parent_stop, child_stops):

    parent_stop.latitude = sum(float(child_stop.latitude) for child_stop in child_stops)/len(child_stops)
    parent_stop.longitude = sum(float(child_stop.longitude) for child_stop in child_stops)/len(child_stops)

    if parent_stop.id is None:
        child_stop_ids = [child_stop.id for child_stop in child_stops]
        parent_stop.id = '-'.join(sorted(child_stop_ids))

    if parent_stop.name is None:
        child_stop_names = {child_stop.name: 0 for child_stop in child_stops}
        for child_stop in child_stops:
            child_stop_names[child_stop.name] += 1
        max_freq = max(child_stop_names.values())
        most_frequent_names = set()
        for child_stop_name, freq in child_stop_names.items():
            if freq == max_freq:
                most_frequent_names.add(child_stop_name)

        for name in most_frequent_names.copy():
            remove = False
            for other_name in most_frequent_names:
                if name != other_name and name in other_name:
                    remove = True
            if remove:
                most_frequent_names.remove(name)
        parent_stop.name = ' / '.join(sorted(most_frequent_names))


def _import_static_data(system):

    package = importlib.import_module(system.package)
    system_base_dir = os.path.dirname(package.__file__)
    agency_data_dir = os.path.join(system_base_dir, 'agencydata')
    custom_data_dir = os.path.join(system_base_dir, 'customdata')

    config_file_path = os.path.join(system_base_dir, 'config.yaml')
    system_config = SystemConfig(config_file_path)

    gtfs_static_parser = gtfsstaticutil.GtfsStaticParser()
    gtfs_static_parser.parse_from_directory(agency_data_dir)

    for route in gtfs_static_parser.route_id_to_route.values():
        route.system = system

    # next 3 bits: Construct larger stations using transfers.txt
    # TODO: make a separate method
    station_sets_by_stop_id = {}
    for stop in gtfs_static_parser.stop_id_to_stop.values():
        stop.system = system
        if not stop.is_station:
            parent_stop = gtfs_static_parser.stop_id_to_stop.get(stop.parent_stop_id, None)
            if parent_stop is None:
                stop.is_station = True
            else:
                stop.parent_stop = parent_stop
        if stop.is_station:
            station_sets_by_stop_id[stop.id] = {stop.id}

    for (stop_id_1, stop_id_2) in gtfs_static_parser.transfer_tuples:
        updated_station_set = station_sets_by_stop_id[stop_id_1].union(
            station_sets_by_stop_id[stop_id_2])
        for stop_id in updated_station_set:
            station_sets_by_stop_id[stop_id] = updated_station_set

    for station_set in station_sets_by_stop_id.values():
        if len(station_set) <= 1:
            continue
        parent_stop = models.Stop()
        child_stops = [gtfs_static_parser.stop_id_to_stop[stop_id] for stop_id in station_set]
        for child_stop in child_stops:
            child_stop.parent_stop = parent_stop
        _lift_stop_properties(parent_stop, child_stops)
        parent_stop.is_station = True
        parent_stop.system = system

        station_set.clear()

    for stop_alias in gtfs_static_parser.stop_id_alias_to_stop_alias.values():
        stop_id = stop_alias.stop_id
        stop = gtfs_static_parser.stop_id_to_stop[stop_id]
        stop_alias.stop = stop

    servicepatternmanager.construct_sps_from_gtfs_static_data(
        gtfs_static_parser,
        system_config.static_route_sps,
        system_config.static_other_sps,
    )

    direction_name_rules_files = system_config.direction_name_rules_files
    priority = 0
    for direction_name_rules_file_path in direction_name_rules_files:
        full_path = os.path.join(custom_data_dir, direction_name_rules_file_path)
        with open(full_path) as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                # TODO: allow either stop_id or stop_id alias
                stop_id = row['stop_id']
                stop = gtfs_static_parser.stop_id_to_stop.get(stop_id, None)
                if stop is None:
                    continue
                direction_id = row.get('direction_id', None)
                if direction_id is not None:
                    direction_id = (direction_id == '0')
                direction_name_rule = models.DirectionNameRule()
                direction_name_rule.stop = stop
                direction_name_rule.priority = priority
                direction_name_rule.direction_id = direction_id
                direction_name_rule.track = row.get('track', None)
                direction_name_rule.stop_id_alias = row.get('stop_id_alias', None)
                direction_name_rule.name = row['direction_name']
                priority += 1

    for feed_config in system_config.feeds:
        feed = models.Feed()
        feed.system = system
        feed.id = feed_config['name']
        feed.url = feed_config['url'].format(**system_config.env_vars)
        feed.parser = feed_config['parser']
        if feed.parser == 'custom':
            feed.custom_module = feed_config['custom_parser']['module']
            feed.custom_function = feed_config['custom_parser']['function']


class SystemConfig:

    def __init__(self, config_file_path):
        with open(config_file_path, 'r') as f:
            self.config = yaml.load(f)
        self.feeds = self.config.get('feeds', None)
        self.static_route_sps = self.config.get(
            'static_route_service_patterns', [])
        self.static_other_sps = self.config.get(
            'static_other_service_patterns', [])
        self.realtime_route_sps = self.config.get(
            'realtime_route_service_patterns',
            {'enabled': False})
        self.direction_name_rules_files = self.config.get(
            'direction_name_rules_files', [])

        self.env_vars = {}
        env_vars_config = self.config.get('environment_variables', {})
        for key, value in env_vars_config.items():
            if value not in os.environ:
                # TODO: make this a Transiter spefic exeption type
                raise KeyError('Missing env var {}'.format(value))
            self.env_vars[key] = os.environ.get(value, None)

