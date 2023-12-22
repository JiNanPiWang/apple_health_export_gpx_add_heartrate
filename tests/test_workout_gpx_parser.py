import unittest
import datetime

from src.workout_gpx_parser import WorkoutGpxParser
from src.gpx_data_point import GpxDataPoint


class TestWorkoutGpxParser(unittest.TestCase):
    def test_parse_data(self):
        parser = WorkoutGpxParser('route_2019-10-03_8.53am.gpx')
        for i, data_point in enumerate(parser.get_full_data(), start=1):
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
                # print(f'Lon: {lon}, Lat: {lat}, Elevation: {ele}, Time: {time}, Speed: {speed}')

    def test_with_single_gpx_data(self):
        # 测试，将WorkoutGpxParser的内容转换为SingleGpxData的格式
        parser = WorkoutGpxParser('route_2019-10-03_8.53am.gpx')
        gpx_items: list[GpxDataPoint] = []
        for item in parser.get_full_data_in_dict():
            gpx_items.append(GpxDataPoint(
                lon=item['lon'],
                lat=item['lat'],
                ele=item['ele'],
                time=item['time'],
            ))
        self.assertEqual(gpx_items[4 - 1].lon, "114.305786")
        self.assertEqual(gpx_items[4 - 1].ele, "27.656521")
        self.assertEqual(gpx_items[4 - 1].datetime_utc0.date(), datetime.date(2019, 10, 3))
        self.assertEqual(gpx_items[4 - 1].datetime_utc0.time(), datetime.time(0, 50, 6))


if __name__ == '__main__':
    unittest.main()
