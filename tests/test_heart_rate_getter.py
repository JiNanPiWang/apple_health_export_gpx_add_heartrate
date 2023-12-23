import os.path
import unittest
from datetime import datetime, timezone

from src.heart_rate_getter import HeartRateGetter
from config.paths import WORKOUT_ROUTES


class MyTestCase(unittest.TestCase):
    def test_get_heartrate_list(self):
        file_path = os.path.join(WORKOUT_ROUTES, 'route_2019-10-03_4.05pm.gpx')
        heart_rate_getter = HeartRateGetter(file_path=file_path)
        tmp_time = datetime(2019, 10, 3, 8, 2, 21)
        tmp_time = tmp_time.replace(tzinfo=timezone.utc)
        self.assertEqual(int(heart_rate_getter.heartrate_dict[tmp_time]),
                         91)
        pass


    def test_get_heartrate_list1(self):
        heart_rate_getter = HeartRateGetter(None, file_name='route_2019-10-03_4.05pm.gpx')
        tmp_time = datetime(2019, 10, 3, 8, 2, 21)
        tmp_time = tmp_time.replace(tzinfo=timezone.utc)
        self.assertEqual(int(heart_rate_getter.heartrate_dict[tmp_time]),
                         91)
        pass


if __name__ == '__main__':
    unittest.main()
