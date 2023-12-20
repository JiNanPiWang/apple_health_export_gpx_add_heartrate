import json
import os
from config.paths import WORKOUT_ROUTES
from utils.strava_utils import make_strava_client, upload_file_to_strava


def upload_gpx_to_strava(file_path: str):
    with open("config/strava_config.json", 'r') as f:
        strava_config = json.load(f)
    client = make_strava_client(
        strava_config["client_id"], strava_config["client_secret"], strava_config["refresh_token"]
    )
    upload_file_to_strava(client, file_path, 'gpx', 'Ride')