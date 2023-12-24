# 在export.xml中，有一个workout标签，如<Workout workoutActivityType="HKWorkoutActivityTypeWalking"，
# 可以通过它来判断运动类型
# 传入全部的workout-routes-run文件夹，返回一个字典，key为文件名，value为运动类型
# 文件名称使用endDate确定

import os

from config.paths import WORKOUT_ROUTES
from .export_xml_parser import ExportXmlParser
from config.activity_types import type_trans
from datetime import datetime, timezone, timedelta
from .gpx_data_point import GpxDataPoint


def parse_date_to_filename(end_date):
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


def parse_date_from_filename(file_name):
    """
    Parse date from file name like
    route_2019-10-04_9.45am.gpx -> 2019-10-04 09:45:05
    route_2019-10-03_4.05pm.gpx -> 2019-10-03 16:05:59
    :param file_name: str
    :return: end_date
    """
    _date = GpxDataPoint(time=file_name[6:-4]).datetime_origin
    # 格式转换为utc+8，datetime比较时间会自动转换到同一时区，所以无需考虑过多内容
    _date = _date.replace(tzinfo=timezone(timedelta(hours=8)))
    return _date


# TODO: 很多activity type都找不到，如果时间在startDate和endDate之间，就将中间的activity type设为这个activity type
# 比如route_2019-10-23_12.08pm，但creation_date和end_date都是2019-10-23 12:09
def get_sport_type(files: list[str]):
    print('Start getting workout type for all files')
    type_dict = {}
    for record in ExportXmlParser().load_activities_type_in_dict(files):
        # record be like:
        # {
        #     'activity_type':'HKWorkoutActivityTypeCycling',
        #     'end_date':'2019-10-03 08:53:38 +0800'
        # }
        file_name = parse_date_to_filename(record['end_date'])
        try:
            strava_type = type_trans[record['activity_type']]
        except KeyError:
            print('Unsupported activity type, you can change its type in strava manually.\n'
                  f'{file_name}\'s type default set to workout type')
            strava_type = 'Workout'
        type_dict[file_name] = strava_type

    # TODO：在最后遍历所有文件，如果文件不在字典中，就找时间在startDate和endDate之间

    print('Successfully get workout type for all files')
    return type_dict

