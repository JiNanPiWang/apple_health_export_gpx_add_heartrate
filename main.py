import argparse
import os

from src.gpx_merger import GpxMerger
from config.paths import WORKOUT_ROUTES
from src.strava_gpx_uploader import StravaGpxUploader
from src.export_xml_parser import ExportXmlParser
from src.sport_type_getter import get_sport_type

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

    workout_type = get_sport_type(files)

    for i, gpx_file in enumerate(files):
        if i == 2:
            break
        # custom your desired time
        year, month, day = int(gpx_file[6:10]), int(gpx_file[11:13]), int(gpx_file[14:16])
        if year > 2019:
            break

        print(f'Now processing {gpx_file}')
        new_gpx = GpxMerger(gpx_file)
        new_gpx.merge_points()
        new_gpx.save_gpx()
        if options.upload_to_strava:
            Uploader = StravaGpxUploader(new_gpx.new_file_path, workout_type[gpx_file])
            Uploader.upload_gpx()
