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
        self.access_token = strava_config["access_token"]
        self.client = get_strava_client(self.access_token)

    def upload(self):
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
