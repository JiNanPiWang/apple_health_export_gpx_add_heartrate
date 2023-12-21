import time

from stravalib.client import Client
from stravalib.exc import RateLimitExceeded
from datetime import datetime


def make_strava_client(client_id, client_secret, refresh_token):
    """
    用于生成strava client，将内容上传到你的账户
    Used to generate a strava client to upload content to your account
    """
    client = Client()

    refresh_response = client.refresh_access_token(
        client_id=client_id, client_secret=client_secret, refresh_token=refresh_token
    )
    client.access_token = refresh_response["access_token"]
    return client


# 需要定义传入activity_type，否则默认Ride
# possible values: Ride, run, swim, workout, hike, walk, nordicski
def upload_file_to_strava(client, file_name, data_type, activity_type='Ride', private=True):
    """
    用于上传文件到strava
    Used to upload files to strava
    """
    with open(file_name, "rb") as f:
        try:
            r = client.upload_activity(
                activity_file=f, data_type=data_type, activity_type=activity_type, private=private
            )

        except RateLimitExceeded as e:
            timeout = e.timeout
            print()
            print(f"Strava API Rate Limit Exceeded. Retry after {timeout} seconds")
            print()
            time.sleep(timeout)
            r = client.upload_activity(
                activity_file=f, data_type=data_type, activity_type=activity_type
            )
        print(
            f"Uploading {data_type} file: {file_name} to strava, upload_id: {r.upload_id}."
        )
