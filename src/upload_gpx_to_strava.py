import json
import os
from config.paths import WORKOUT_ROUTES
from utils.strava_utils import make_strava_client, upload_file_to_strava


def upload_gpx_to_strava(file_path: str):
    with open("config/strava_config.json", 'r') as f:
        strava_config = json.load(f)

    # Edit access_token in the strava_config.json or edit here
    # like access_token = '***'
    access_token = strava_config["access_token"]

    client = make_strava_client(
        strava_config["client_id"], strava_config["client_secret"], strava_config["refresh_token"]
    )
    upload_file_to_strava(client, file_path, 'gpx', strava_config["activity_type"], True)