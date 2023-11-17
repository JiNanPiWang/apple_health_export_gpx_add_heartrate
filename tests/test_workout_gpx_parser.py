import unittest
from workout_gpx_parser import WorkoutGpxParser


class TestWorkoutGpxParser(unittest.TestCase):
    def test_parse_data(self):
        parser = WorkoutGpxParser('route_2019-10-03_8.53am.gpx')
        for i, data_point in enumerate(parser.parse_data(), start=1):
            if i == 4:
                lon, lat, ele, time, speed = data_point
                # 在这里执行你的处理逻辑，例如打印或保存数据
                self.assertEqual(lon, "114.305786")
                self.assertEqual(lat, "30.644611")
                self.assertEqual(ele, "27.656521")
                self.assertEqual(time, "2019-10-03T00:50:06Z")
                self.assertEqual(speed, "2.950589")
                print(f'Lon: {lon}, Lat: {lat}, Elevation: {ele}, Time: {time}, Speed: {speed}')


if __name__ == '__main__':
    unittest.main()
