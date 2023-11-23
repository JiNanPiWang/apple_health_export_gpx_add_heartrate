import unittest
import datetime

from export_xml_parser import ExportXmlParser


class TestExportXmlParser(unittest.TestCase):
    def test_get_heart_rate(self):
        health_data = ExportXmlParser()
        for record in health_data.get_heart_rate():
            start_date, end_date, value = record
            if start_date[:10] == '2019-10-03':
                self.assertEqual(value, '70')
                break
        for record in health_data.get_heart_rate():
            start_date, end_date, value = record
            if start_date == '2019-10-03 23:53:50 +0800':
                self.assertEqual(value, '52')
                break
