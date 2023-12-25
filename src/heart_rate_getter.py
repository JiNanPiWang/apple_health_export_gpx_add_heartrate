import os.path

from .workout_gpx_parser import WorkoutGpxParser
from .gpx_data_point import GpxDataPoint
from .export_xml_parser import ExportXmlParser
from datetime import datetime, timezone, timedelta
from config.paths import WORKOUT_ROUTES


def get_workout_time(file_path):
    workout_gpx = WorkoutGpxParser(workout_gpx_name=None, workout_gpx_path=file_path)
    time = []
    for item in workout_gpx.get_full_data_in_dict():
        # 确保放入的是规范时间
        datet = GpxDataPoint(time=item['time'])
        time.append(datet.datetime_utc0)
    return time


def get_heartrate_list(workout_time):
    heartrate_list = []

    # 初始化last_datet为一个大值
    last_datet = datetime.max.replace(tzinfo=timezone.utc)
    for item in ExportXmlParser().load_heart_rate_in_dict():
        datet = GpxDataPoint(time=item['creation_date']).datetime_utc0

        if last_datet < workout_time[0] <= datet:
            heartrate_list.append((last_datet, item['value']))
            heartrate_list.append((datet, item['value']))
        elif workout_time[0] <= datet <= workout_time[-1]:
            heartrate_list.append((datet, item['value']))
        elif last_datet <= workout_time[-1] < datet:
            heartrate_list.append((datet, item['value']))
            break

        last_datet = datet
    return heartrate_list

# TODO：部分运动在结束之后，心率才记录，而且后面记录的心率应该是前面的内容，也就是心率数值漂移了
# 比如10月10日9:46am的
def get_heart_dict(workout_time):
    heart_dict = {}

    # 初始化last_datet为一个大值
    last_datet = datetime.max.replace(tzinfo=timezone.utc)
    current_time = workout_time[0]

    for item in ExportXmlParser().load_heart_rate_in_dict():
        datet = GpxDataPoint(time=item['creation_date']).datetime_utc0
        heart_rate = item['value']

        # 记录下对应时间的内容
        # 记录第一个时间点，即上一次还不在内，这一次时间在内
        if last_datet < workout_time[0] <= datet:
            heart_dict[last_datet] = heart_rate
            heart_dict[datet] = heart_rate
            while current_time <= datet:
                heart_dict[current_time] = heart_rate
                current_time += timedelta(seconds=1)

        # 正常情况，时间在范围内
        elif workout_time[0] <= datet <= workout_time[-1]:
            heart_dict[datet] = heart_rate
            while current_time <= datet:
                heart_dict[current_time] = heart_rate
                current_time += timedelta(seconds=1)

        # 最后一个时间点，上一次还在，这一次不在
        elif last_datet <= workout_time[-1] < datet:
            heart_dict[datet] = heart_rate
            while current_time <= datet:
                heart_dict[current_time] = heart_rate
                current_time += timedelta(seconds=1)
            break

        last_datet = datet

    return heart_dict


class HeartRateGetter:
    def __init__(self, file_path, file_name=None):
        if file_name is not None:
            self.file_path = os.path.join(WORKOUT_ROUTES, file_name)
        else:
            self.file_path = file_path
        self.time = get_workout_time(self.file_path)
        # self.heartrate_list = get_heartrate_list(self.time)
        self.heartrate_dict = get_heart_dict(self.time)
        pass
