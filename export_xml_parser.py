# export_xml_parser.py

# 用于解析apple_health_export/导出.xml中的心率信息
# This module contains a parser for extracting health data in apple_health_export/export.xml, including heart rate
# from an Apple Health export XML file.

import xml.etree.ElementTree as ET
import os
import argparse


class HealthExportXmlParser:
    def __init__(self):
        # 当前路径
        self.path = os.path.dirname(__file__)
        # xml路径
        self.health_export_xml_path = os.path.join(self.path, 'apple_health_export/export.xml')
        
        