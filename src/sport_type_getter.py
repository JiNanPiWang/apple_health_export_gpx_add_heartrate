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


# 比如route_2019-10-23_12.08pm，但creation_date和end_date都是2019-10-23 12:09
def get_sport_type(files: list[str]):
    """
    Get workout type for almost all files, exclude files that are uploaded via Strava, etc
    Apple Watch's record is fine
    :param files: list of uploading files
    :return: dict, key is file name, value is workout type
    """
    print('Start getting workout type for all files')
    type_dict = {}
    for record in ExportXmlParser().load_activities_type_in_dict(files):
        # record be like:
        # {
        #     'activity_type':'HKWorkoutActivityTypeCycling',
        #     'end_date':'2019-10-03 08:53:38 +0800'
        # }
        start_date = record['start_date']
        end_date = record['end_date']
        sport_type = record['activity_type']

        date_range = (start_date, end_date)
        type_dict[date_range] = sport_type

    file_types = {}
    for file in files:
        file_time = parse_date_from_filename(file)
        for item in type_dict.items():
            start_date = GpxDataPoint(time=item[0][0]).datetime_origin
            end_date = GpxDataPoint(time=item[0][1]).datetime_origin
            if start_date <= file_time <= end_date:
                file_types[file] = item[1]
                break
        else:
            # Get workout type for almost all files, exclude files that are uploaded via Strava, etc
            # set default type to 'Workout'
            file_types[file] = 'Workout'

    print('Successfully get workout type for all files')
    return file_types
