# export_xml_parser.py

# 用于解析apple_health_export/导出.xml中的心率信息
# This module contains a parser for extracting health data in apple_health_export/export.xml, including heart rate
# from an Apple Health export XML file.

import xml.etree.ElementTree as ET
import os
import argparse

# TODO：先写输出函数，输出一份不要心率的测试一下
class ExportXmlParser:
    def __init__(self):
        # 当前路径
        self.path = os.path.dirname(__file__)
        # 获取项目根目录
        self.project_root = os.path.abspath(os.path.join(self.path, '..'))
        # xml路径
        self.health_export_xml_path = os.path.join(self.project_root, 'apple_health_export/export.xml')

    def load_xml(self):
        with open(self.health_export_xml_path, 'rb') as xml_file:
            for event, elem in ET.iterparse(xml_file, events=('start', 'end')):
                if event == 'start' and elem.tag == 'Record' and elem.get('type') == 'HKQuantityTypeIdentifierHeartRate':
                    start_date = elem.get('startDate')
                    value = elem.get('value')
                    yield start_date, value
