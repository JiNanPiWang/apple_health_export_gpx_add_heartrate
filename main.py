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
        # if i == 3:
        #     break
        year, month, day = eval(gpx_file[6:10]), eval(gpx_file[11:13]), eval(gpx_file[14:16])
        if year > 2019:
            break

        print(f'Now processing {gpx_file}')
        new_gpx = MergeGpxData(gpx_file)
        new_gpx.merge_points()
        new_gpx.save_gpx()
        # if options.upload_to_strava:
        #     Upload = UploadGpxToStrava(new_gpx.new_file_path)
        #     Upload.upload_gpx()
