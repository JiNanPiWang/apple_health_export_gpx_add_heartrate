# workout_gpx_parser.py

# 用于解析apple_health_export/workout-routes/*.gpx
# This module contains a parser for extracting health data in apple_health_export/workout-routes/*.gpx,
# including everything from an Apple Health workout export GPX file.

import xml.etree.ElementTree as ET


class ExportXmlParser:
    def __init__(self, workout_gpx_path):
        self.export_xml_path = f'apple_health_export/workout-routes/{workout_gpx_path}'

    def parse_heart_rate_data(self):
        # 解析导出.xml中的心率数据并返回
        tree = ET.parse(self.export_xml_path)
        root = tree.getroot()

        namespace = {'gpx': 'http://www.topografix.com/GPX/1/1'}

        for trkpt in root.findall('.//trkpt'):
            lon = trkpt.attrib['lon']
            lat = trkpt.attrib['lat']
            ele = trkpt.find('gpx:ele', namespace).text
            time = trkpt.find('gpx:time', namespace).text
            speed = trkpt.find('gpx:extensions/gpx:speed', namespace).text \
                if trkpt.find('gpx:extensions/gpx:speed', namespace) is not None else "N/A"
            yield lon, lat, ele, time, speed

