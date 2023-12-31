# export_xml_parser.py

# 用于解析apple_health_export/导出.xml中的心率信息
# This module contains a parser for extracting health data in apple_health_export/export.xml, including heart rate
# from an Apple Health export XML file.

import xml.etree.ElementTree as ET
import os
from config.paths import PROJECT_ROOT


class ExportXmlParser:
    def __init__(self):
        # xml路径
        self.health_export_xml_path = os.path.join(PROJECT_ROOT, 'apple_health_export/export.xml')

    def load_heart_rate(self):
        """
        Load if record type="HKQuantityTypeIdentifierHeartRate"
        :return yield: start_date, end_date, creation_date, value
        """
        with open(self.health_export_xml_path, 'rb') as xml_file:
            for event, elem in ET.iterparse(xml_file, events=('start', 'end')):
                if event == 'start' and elem.tag == 'Record' and elem.get('type') == 'HKQuantityTypeIdentifierHeartRate':
                    start_date = elem.get('startDate')
                    end_date = elem.get('endDate')
                    creation_date = elem.get('creationDate')
                    value = elem.get('value')
                    yield start_date, end_date, creation_date, value

    def load_heart_rate_in_dict(self):
        """
        Load if record type="HKQuantityTypeIdentifierHeartRate"
        :return yield: start_date, end_date, creation_date, value
        but in dict format
        """
        for record in self.load_heart_rate():
            start_date, end_date, creation_date, value = record
            yield {'start_date': start_date, 'end_date': end_date, 'creation_date': creation_date, 'value': value}

    def load_activities_type(self, files: list[str]):
        """
        Load if tag is 'Workout'
        :param files: list of uploading files
        :return:
        """
        with open(self.health_export_xml_path, 'rb') as xml_file:
            for event, elem in ET.iterparse(xml_file, events=('start', 'end')):
                if event == 'start' and elem.tag == 'Workout':
                    start_date = elem.get('startDate')
                    end_date = elem.get('endDate')
                    activity_type = elem.get('workoutActivityType')
                    yield start_date, end_date, activity_type

    def load_activities_type_in_dict(self, files: list[str]):
        """
        Load if tag is 'Workout'
        :param files: list of uploading files
        :return:
        """
        for record in self.load_activities_type(files):
            start_date, end_date, activity_type = record
            yield {'start_date': start_date, 'end_date': end_date, 'activity_type': activity_type}
