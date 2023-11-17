import unittest
from single_gpx_data import SingleGpxData


class TestSingleGpxData(unittest.TestCase):
    def test_parse_datetime(self):
        time_string1 = "2023-11-12T06:50:58Z"
        time_string2 = "2023-04-05 14:29:00 +0800"
        time_string3 = "2023-04-05 14:29:00 +0800"

        data_point1 = SingleGpxData(time=time_string1)
        data_point2 = SingleGpxData(time=time_string2)
        data_point3 = SingleGpxData(time=time_string3)

        self.assertIsNotNone(data_point1)
        self.assertIsNotNone(data_point2)
        self.assertIsNotNone(data_point3)
        print(data_point1)
        print(data_point2)
        print(data_point3)

        
if __name__ == '__main__':
    unittest.main()
    