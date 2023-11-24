import unittest
import datetime

from export_xml_parser import ExportXmlParser


class TestExportXmlParser(unittest.TestCase):
    def __init__(self, methodName=None, injection=None, warnings=True, dbHelper=None):
        super().__init__(methodName)
        self.injection = injection
        self.warnings = warnings
        self.dbHelper = dbHelper
        self.health_data = ExportXmlParser()

    def test_get_heart_rate(self):
        self.health_data = ExportXmlParser()
        for record in self.health_data.get_heart_rate():
            start_date, end_date, value = record
            if start_date[:10] == '2019-10-03':
                self.assertEqual(value, '70')
                break
        for record in self.health_data.get_heart_rate():
            start_date, end_date, value = record
            if start_date == '2019-10-03 23:53:50 +0800':
                self.assertEqual(value, '52')
                break

    def test_load_xml(self):
        for start_date, value in self.health_data.load_xml():
            if start_date == '2023-09-06 19:35:24 +0800':
                self.assertEqual(value, '154')
            if start_date == '2019-12-05 15:28:13 +0800':
                self.assertEqual(value, '82')
