import os
import unittest
from src.merge_gpx_data import MergeGpxData


class MyTestCase(unittest.TestCase):
    def test_save_gpx(self):
        test = MergeGpxData('test')
        test.save_gpx()
        self.assertEqual(os.path.exists(test.file_path), True)


if __name__ == '__main__':
    unittest.main()
