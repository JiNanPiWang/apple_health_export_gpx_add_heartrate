import os
import unittest

from config.paths import WORKOUT_ROUTES
from src.sport_type_getter import get_sport_type


class MyTestCase(unittest.TestCase):
    def test_get_sport_type(self):
        files = os.listdir(WORKOUT_ROUTES)

        workout_type = get_sport_type(files)

        self.assertEqual(workout_type[files[0]], 'Ride')
        self.assertEqual(workout_type['route_2019-11-15_6.49am.gpx'], 'Run')


if __name__ == '__main__':
    unittest.main()
