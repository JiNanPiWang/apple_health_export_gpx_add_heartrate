import unittest
from workout_gpx_parser import WorkoutGpxParser


class TestWorkoutGpxParser(unittest.TestCase):
    def test_parse_data(self):
        parser = WorkoutGpxParser('route_2019-10-03_8.53am.gpx')
        for i, data_point in enumerate(parser.parse_data(), start=1):
            if i == 4:
                lon, lat, ele, time, speed, course, hAcc, vAcc = data_point
                self.assertEqual(lon, "114.305786")
                self.assertEqual(lat, "30.644611")
                self.assertEqual(ele, "27.656521")
                self.assertEqual(time, "2019-10-03T00:50:06Z")
                self.assertEqual(speed, "2.950589")
                self.assertEqual(course, "214.804688")
                self.assertEqual(hAcc, "1.683047")
                self.assertEqual(vAcc, "1.133000")
                print(f'Lon: {lon}, Lat: {lat}, Elevation: {ele}, Time: {time}, Speed: {speed}')

    def test_get_lat_data(self):
        parser = WorkoutGpxParser('route_2019-10-03_8.53am.gpx')
        for i, data in enumerate(parser.get_lat_data(), start=1):
            if i == 6:
                self.assertEqual(data, '30.644586')

    def test_get_time_data(self):
        parser = WorkoutGpxParser('route_2019-10-03_8.53am.gpx')
        for i, data in enumerate(parser.get_time_data(), start=1):
            if i == 6:
                self.assertEqual(data, '2019-10-03T00:50:08Z')


if __name__ == '__main__':
    unittest.main()
