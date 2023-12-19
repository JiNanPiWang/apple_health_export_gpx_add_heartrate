import os

import gpxpy
from src.workout_gpx_parser import WorkoutGpxParser
from src.single_gpx_data import SingleGpxData
from src.merge_gpx_data import MergeGpxData
from src.config import PROJECT_ROOT, WORKOUT_ROUTES
import xml.etree.ElementTree as ET


if __name__ == '__main__':
    files = os.listdir(WORKOUT_ROUTES)

    # 打印所有文件名
    for gpx_file in files:
        print(gpx_file)

        new_gpx = MergeGpxData(gpx_file)
        new_gpx.merge_points()
        new_gpx.save_gpx()

# TODO: 自动上传到strava
        break
