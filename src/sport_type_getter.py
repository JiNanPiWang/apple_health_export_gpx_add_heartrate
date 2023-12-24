# 在export.xml中，有一个workout标签，如<Workout workoutActivityType="HKWorkoutActivityTypeWalking"，
# 可以通过它来判断运动类型
# 传入全部的workout-routes-run文件夹，返回一个字典，key为文件名，value为运动类型
# 文件名称使用endDate确定

import os

from config.paths import WORKOUT_ROUTES
from .export_xml_parser import ExportXmlParser
from config.activity_types import type_trans
from datetime import datetime
from .gpx_data_point import GpxDataPoint


def parse_date(end_date):
    """
    Parse date from end_date to file name like
    2019-10-04 09:45:05 +0800 -> route_2019-10-04_9.45am.gpx
    2019-10-03 16:05:59 +0800 -> route_2019-10-03_4.05pm.gpx
    :param end_date: str, later trans to datetime.datetime
    :return: file_name
    """
    _date = GpxDataPoint(time=end_date).datetime_origin
    
    # 解读：小时使用%#I：12小时制，#使得小时前面不带0，使用%H则是24小时制；%p：AM/PM，lower()，将%P转为小写
    parsed_date = _date.strftime("%Y-%m-%d_%#I.%M%p").lower()
    file_name = f'route_{parsed_date}.gpx'
    return file_name


def get_sport_type(files: list[str]):
    type_dict = {}
    for record in ExportXmlParser().load_activities_type_in_dict(files):
        # record be like:
        # {
        #     'activity_type':'HKWorkoutActivityTypeCycling',
        #     'end_date':'2019-10-03 08:53:38 +0800'
        # }
        file_name = parse_date(record['end_date'])
        try:
            strava_type = type_trans[record['activity_type']]
        except KeyError:
            print('Unsupported activity type, you can change its type in strava manually.\n'
                  f'{file_name}\'s type set default to workout type')
            strava_type = 'Workout'
        type_dict[file_name] = strava_type
    return type_dict
