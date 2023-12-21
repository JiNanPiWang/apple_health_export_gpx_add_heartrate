import json
import os
import time

from config.paths import WORKOUT_ROUTES
from utils.strava_utils import make_strava_client, upload_file_to_strava
from stravalib.util.limiter import RateLimiter, XRateLimitRule
from stravalib.client import Client, exc
from utils.exceptions import RateLimitException

def get_strava_client(access_token):
    token = access_token
    rate_limiter = RateLimiter()
    rate_limiter.rules.append(XRateLimitRule(
        {'short': {'usageFieldIndex': 0, 'usage': 0,
                   # 60s * 15 = 15 min
                   'limit': 100, 'time': (60 * 15),
                   'lastExceeded': None, },
         'long': {'usageFieldIndex': 1, 'usage': 0,
                  # 60s * 60m * 24 = 1 day
                  'limit': 1000, 'time': (60 * 60 * 24),
                  'lastExceeded': None}}))
    client = Client(rate_limiter=rate_limiter)
    client.access_token = token
    return client


class UploadGpxToStrava:
    def __init__(self, file_path: str):
        with open("config/strava_config.json", 'r') as f:
            strava_config = json.load(f)

        # Edit access_token in the strava_config.json or edit here
        # like access_token = '***'
        self.file_path = file_path
        self.access_token = strava_config["access_token"]
        self.activity_type = strava_config["activities_type"]
        self.client = get_strava_client(self.access_token)

    def get_athlete_name(self):
        athlete = None
        for i in range(2):
            try:
                athlete = self.client.get_athlete()
            except exc.RateLimitExceeded as err:
                if i > 0:
                    raise RateLimitException("Daily Rate limit exceeded")
                print("Rate limit exceeded in connecting - Retrying strava connection in 15 minutes")
                time.sleep(900)
                continue
            break

        print("Now authenticated for " + athlete.firstname + " " + athlete.lastname)

    # client, gpxfile, strava_activity_type, notes
    def upload_gpx(self):
        gpxfile = self.file_path
        if not os.path.isfile(gpxfile):
            print("No file found for " + gpxfile + "!")
            return False

        print("Uploading " + gpxfile)

        for i in range(2):
            try:
                upload = self.client.upload_activity(
                    activity_file=open(gpxfile, 'r'),
                    data_type='gpx',
                    private=True,
                    activity_type=self.activity_type
                )
            except exc.RateLimitExceeded as err:
                if i > 0:
                    raise RateLimitException("Daily Rate limit exceeded - exiting program")
                print("Rate limit exceeded in uploading - pausing uploads for 15 minutes to avoid rate-limit")
                time.sleep(900)
                continue
