# workout_gpx_parser.py

# 用于解析apple_health_export/workout-routes/*.gpx
# This module contains a parser for extracting health data in apple_health_export/workout-routes/*.gpx,
# including everything from an Apple Health workout export GPX file.

import xml.etree.ElementTree as ET
import os


class WorkoutGpxParser:
    def __init__(self, workout_gpx_name):
        # argument: workout_gpx name
        # 当前路径
        self.path = os.path.dirname(__file__)

        # gpx路径
        self.workout_gpx_path = os.path.join(self.path, 'apple_health_export/workout-routes', workout_gpx_name)

        # 获取GPX的信息
        self.tree = ET.parse(self.workout_gpx_path)
        self.root = self.tree.getroot()
        self.namespace = {'gpx': 'http://www.topografix.com/GPX/1/1'}

    # 获取GPX的所有数据（生成器）
    def parse_data(self):
        for trkpt in self.root.findall('.//gpx:trkpt', self.namespace):
            lon = trkpt.attrib['lon']
            lat = trkpt.attrib['lat']
            ele = trkpt.find('gpx:ele', self.namespace).text
            time = trkpt.find('gpx:time', self.namespace).text
            speed = trkpt.find('gpx:extensions/gpx:speed', self.namespace).text \
                if trkpt.find('gpx:extensions/gpx:speed', self.namespace) is not None else "N/A"
            yield lon, lat, ele, time, speed

    # 单独获取GPX的数据
    def get_lon_data(self):
        for trkpt in self.parse_data():
            lon, _, _, _, _ = trkpt
            yield lon

    def get_lat_data(self):
        for trkpt in self.parse_data():
            _, lat, _, _, _ = trkpt
            yield lat

    def get_elevation_data(self):
        for trkpt in self.parse_data():
            _, _, ele, _, _ = trkpt
            yield ele

    def get_time_data(self):
        for trkpt in self.parse_data():
            _, _, _, time, _ = trkpt
            yield time

    def get_speed_data(self):
        for trkpt in self.parse_data():
            _, _, _, _, speed = trkpt
            yield speed
