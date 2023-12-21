import os
import json

from src.merge_gpx_data import MergeGpxData
from config.paths import WORKOUT_ROUTES
from src.upload_gpx_to_strava import UploadGpxToStrava

if __name__ == '__main__':
    files = os.listdir(WORKOUT_ROUTES)

    # 打印所有文件名
    for gpx_file in files:
        print(gpx_file)

        new_gpx = MergeGpxData(gpx_file)
        new_gpx.merge_points()
        new_gpx.save_gpx()
        upload_to_strava = UploadGpxToStrava(new_gpx.new_file_path)
        upload_to_strava.upload_gpx()

        break
