import os
import unittest
from datetime import timezone

from config.paths import WORKOUT_ROUTES
from src.sport_type_getter import *
from src.gpx_data_point import GpxDataPoint


class MyTestCase(unittest.TestCase):
    def test_get_sport_type(self):
        files = os.listdir(WORKOUT_ROUTES)

        workout_type = get_sport_type(files)

        self.assertEqual(workout_type[files[0]], 'Ride')
        self.assertEqual(workout_type['route_2019-11-15_6.49am.gpx'], 'Run')

    def test_get_sport_type_exist(self):
        files = os.listdir(WORKOUT_ROUTES)

        workout_type = get_sport_type(files)

        for file in files:
            self.assertTrue(file in workout_type.keys())

    def test_parse_date_from_filename(self):
        self.assertLess(parse_date_from_filename('route_2019-10-04_9.45pm.gpx'),
                        GpxDataPoint(time='2019-10-23 12:09:05 +0800').datetime_origin)
        self.assertEqual(parse_date_from_filename('route_2019-10-04_9.45pm.gpx'),
                         GpxDataPoint(time='2019-10-04 21:45:00 +0800').datetime_origin)
        # datetime比较时间会自动转换到同一时区
        self.assertEqual(parse_date_from_filename('route_2019-10-04_9.45pm.gpx'),
                         GpxDataPoint(time='2019-10-04 21:45:00 +0800').datetime_utc0)


if __name__ == '__main__':
    unittest.main()
