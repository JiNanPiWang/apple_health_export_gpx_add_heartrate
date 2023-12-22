import argparse
import os

from src.merge_gpx_data import MergeGpxData
from config.paths import WORKOUT_ROUTES
from src.upload_gpx_to_strava import UploadGpxToStrava

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--upload-to-strava",
        dest="upload_to_strava",
        action="store_true",
        help="get all keep data to gpx and download",
    )
    options = parser.parse_args()

    files = os.listdir(WORKOUT_ROUTES)
    for i, gpx_file in enumerate(files):
        print(f'Now processing {gpx_file}')
        new_gpx = MergeGpxData(gpx_file)
        new_gpx.merge_points()
        new_gpx.save_gpx()
        if options.upload_to_strava:
            upload_to_strava = UploadGpxToStrava(new_gpx.new_file_path)
            upload_to_strava.upload_gpx()
        if i == 2:
            break
