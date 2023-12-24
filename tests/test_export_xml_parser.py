import os
import unittest

from config.paths import WORKOUT_ROUTES
from src.export_xml_parser import ExportXmlParser


class TestExportXmlParser(unittest.TestCase):
    def __init__(self, methodName=None, injection=None, warnings=True, dbHelper=None):
        super().__init__(methodName)
        self.injection = injection
        self.warnings = warnings
        self.dbHelper = dbHelper
        self.health_data = ExportXmlParser()

    def load_heart_rate(self):
        for start_date, end_date, creation_date, value in self.health_data.load_heart_rate():
            if start_date == '2023-09-06 19:35:24 +0800':
                self.assertEqual(value, '154')
            if start_date == '2019-12-05 15:28:13 +0800':
                self.assertEqual(value, '82')

    def test_load_activities_type(self):
        for x in self.health_data.load_activities_type_in_dict(os.listdir(WORKOUT_ROUTES)):
            print(x)

        # self.assertEqual(self.health_data.load_activities_type(), 115)
