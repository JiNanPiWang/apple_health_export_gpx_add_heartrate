import os.path
import unittest
from src.heart_rate_getter import HeartRateGetter
from config.paths import WORKOUT_ROUTES


class MyTestCase(unittest.TestCase):
    def test_get_heartrate_list(self):
        file_path = os.path.join(WORKOUT_ROUTES, 'route_2019-10-03_4.05pm.gpx')
        heart_rate_getter = HeartRateGetter(file_path=file_path)
        pass


if __name__ == '__main__':
    unittest.main()
