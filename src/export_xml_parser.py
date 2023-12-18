# export_xml_parser.py

# 用于解析apple_health_export/导出.xml中的心率信息
# This module contains a parser for extracting health data in apple_health_export/export.xml, including heart rate
# from an Apple Health export XML file.

import xml.etree.ElementTree as ET
import os
# 使用.config，不是config，要不然报错无法import config
from .config import PROJECT_ROOT

class ExportXmlParser:
    def __init__(self):
        # xml路径
        self.health_export_xml_path = os.path.join(PROJECT_ROOT, 'apple_health_export/export.xml')

    def load_xml(self):
        with open(self.health_export_xml_path, 'rb') as xml_file:
            for event, elem in ET.iterparse(xml_file, events=('start', 'end')):
                if event == 'start' and elem.tag == 'Record' and elem.get('type') == 'HKQuantityTypeIdentifierHeartRate':
                    start_date = elem.get('startDate')
                    value = elem.get('value')
                    yield start_date, value
