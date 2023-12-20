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


# TODO：看一下为什么默认是跑步，作用是什么
def get_strava_last_time(client, is_milliseconds=True):
    """
    从 Strava 客户端获取最后一次跑步活动的时间，并根据需要将时间转换为毫秒。如果出现异常或者没有找到符合条件的活动，函数会返回 0。
    if there is no activities cause exception return 0
    """
    try:
        activity = None
        activities = client.get_activities(limit=10)
        activities = list(activities)
        activities.sort(key=lambda x: x.start_date, reverse=True)
        for a in activities:
            if a.type == "Run":
                activity = a
                break
        else:
            return 0
        end_date = activity.start_date + activity.elapsed_time
        last_time = int(datetime.timestamp(end_date))
        if is_milliseconds:
            last_time = last_time * 1000
        return last_time
    except Exception as e:
        print(f"Something wrong to get last time err: {str(e)}")
        return 0


# 需要定义传入activity_type，否则默认Ride
# possible values: Ride, run, swim, workout, hike, walk, nordicski
def upload_file_to_strava(client, file_name, data_type, activity_type='Ride'):
    """
    用于上传文件到strava
    Used to upload files to strava
    """
    with open(file_name, "rb") as f:
        try:
            r = client.upload_activity(
                activity_file=f, data_type=data_type, activity_type=activity_type
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
