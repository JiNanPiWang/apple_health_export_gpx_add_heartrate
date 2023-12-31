# workout_gpx_parser.py

# 用于解析apple_health_export/workout-routes/*.gpx
# This module contains a parser for extracting health data in apple_health_export/workout-routes/*.gpx,
# including everything from an Apple Health workout export GPX file.

import xml.etree.ElementTree as ET
import os
from config.paths import WORKOUT_ROUTES


class WorkoutGpxParser:
    def __init__(self, workout_gpx_name, workout_gpx_path=None):
        # gpx路径
        if workout_gpx_path is not None or workout_gpx_name is None:
            self.workout_gpx_path = workout_gpx_path
        else:
            self.workout_gpx_path = os.path.join(WORKOUT_ROUTES, workout_gpx_name)

        # 获取GPX的信息
        with open(self.workout_gpx_path, 'r') as gpx_file:
            self.tree = ET.parse(gpx_file)
        self.root = self.tree.getroot()
        self.namespace = {'gpx': 'http://www.topografix.com/GPX/1/1'}

    # 获取GPX的所有数据（生成器）
    def get_full_data(self):
        for trkpt in self.root.findall('.//gpx:trkpt', self.namespace):
            try:
                lon = trkpt.attrib['lon']
                lat = trkpt.attrib['lat']
            except KeyError:
                raise KeyError('GPX file is not valid, longitude or latitude is missing')

            ele = trkpt.find('gpx:ele', self.namespace).text
            time = trkpt.find('gpx:time', self.namespace).text
            if ele is None or time is None:
                raise ValueError('GPX file is not valid, elevation or time is missing')

            speed = trkpt.find('gpx:extensions/gpx:speed', self.namespace).text \
                if trkpt.find('gpx:extensions/gpx:speed', self.namespace) is not None else None
            course = trkpt.find('gpx:extensions/gpx:course', self.namespace).text \
                if trkpt.find('gpx:extensions/gpx:course', self.namespace) is not None else None
            hAcc = trkpt.find('gpx:extensions/gpx:hAcc', self.namespace).text \
                if trkpt.find('gpx:extensions/gpx:hAcc', self.namespace) is not None else None
            vAcc = trkpt.find('gpx:extensions/gpx:vAcc', self.namespace).text \
                if trkpt.find('gpx:extensions/gpx:vAcc', self.namespace) is not None else None
            yield lon, lat, ele, time, speed, course, hAcc, vAcc

    # 用字典型获取GPX的所有数据（生成器）
    def get_full_data_in_dict(self):
        for trkpt in self.get_full_data():
            lon, lat, ele, time, speed, course, hAcc, vAcc = trkpt
            yield {'lon': lon, 'lat': lat, 'ele': ele, 'time': time, 'speed': speed, 'course': course,
                   'hAcc': hAcc, 'vAcc': vAcc}
