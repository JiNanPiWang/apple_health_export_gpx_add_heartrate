# test_single_gpx_data.py
# unittest for single_gpx_data.py functions


import datetime
import unittest

from src.single_gpx_data import SingleGpxData


class TestSingleGpxData(unittest.TestCase):
    def test_parse_datetime(self):
        # 测试parse_datetime
        time_string1 = "2023-11-12T06:50:58Z"
        time_string2 = "2023-04-05 14:29:00 +0800"
        time_string3 = "2023-04-05 14:29:00 +0800"

        data_point1 = SingleGpxData(time=time_string1).parse_datetime(time_string1)
        data_point2 = SingleGpxData(time=time_string2).parse_datetime(time_string2)
        data_point3 = SingleGpxData(time=time_string3).parse_datetime(time_string3)

        # 测试时间是否生成 test if time is correct produced
        self.assertIsNotNone(data_point1)
        self.assertIsNotNone(data_point2)
        self.assertIsNotNone(data_point3)
        # 测试时间是否正确 test if time is correct
        self.assertEqual(data_point1.date(), datetime.date(2023, 11, 12))
        self.assertEqual(data_point2.time(), datetime.time(14, 29, 0))
        self.assertEqual(data_point3.tzinfo, datetime.timezone(datetime.timedelta(seconds=8*60*60)))

    def test_convert_to_utc0(self):
        time_string1 = "2023-11-12T06:50:58Z"
        time_string2 = "2023-04-05 04:29:00 +0800"
        time_string3 = "2023-04-05 14:29:00 +0800"

        # 得到utc_0的datetime
        data1 = SingleGpxData(time=time_string1)
        data1.convert_to_utc0(data1.datetime_origin)
        data2 = SingleGpxData(time=time_string2)
        data2.convert_to_utc0(data2.datetime_origin)
        data3 = SingleGpxData(time=time_string3)
        data3.convert_to_utc0(data3.datetime_origin)

        self.assertIsNotNone(data1)
        self.assertIsNotNone(data2)
        self.assertIsNotNone(data3)
        self.assertEqual(data1.datetime_utc0.date(), datetime.date(2023, 11, 12))
        self.assertEqual(data2.datetime_utc0.date(), datetime.date(2023, 4, 4))
        self.assertEqual(data2.datetime_utc0.time(), datetime.time(20, 29, 00))

        
if __name__ == '__main__':
    unittest.main()
    