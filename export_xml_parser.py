# export_xml_parser.py

# 用于解析apple_health_export/导出.xml中的心率信息
# This module contains a parser for extracting health data in apple_health_export/export.xml, including heart rate
# from an Apple Health export XML file.

import xml.etree.ElementTree as ET
import os
import argparse


class ExportXmlParser:
    def __init__(self):
        # 当前路径
        self.path = os.path.dirname(__file__)
        # xml路径
        self.health_export_xml_path = os.path.join(self.path, 'apple_health_export/export.xml')

        # 获取xml的信息
        with open(self.health_export_xml_path, 'r', encoding='utf-8') as xml_file:
            self.tree = ET.parse(xml_file)
        self.root = self.tree.getroot()

    def load_xml(self):
        with open(self.health_export_xml_path, 'rb') as xml_file:
            for event, elem in ET.iterparse(xml_file, events=('start', 'end')):
                if event == 'start' and elem.tag == 'Record' and elem.get('type') == 'HKQuantityTypeIdentifierHeartRate':
                    start_date = elem.get('startDate')
                    value = elem.get('value')
                    yield start_date, value

                # 清理已处理的元素，以释放内存
                elem.clear()

    def get_heart_rate(self):
        for record in self.root.findall('.//Record[@type="HKQuantityTypeIdentifierHeartRate"]'):
            start_date = record.attrib.get('startDate')
            end_date = record.attrib.get('endDate')
            value = record.attrib.get('value')
            yield start_date, end_date, value
