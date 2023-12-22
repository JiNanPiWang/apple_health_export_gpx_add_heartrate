from .workout_gpx_parser import WorkoutGpxParser
from .gpx_data_point import GpxDataPoint
from .export_xml_parser import ExportXmlParser
from datetime import datetime, timezone, timedelta


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
    last_datet = datetime.max.replace(tzinfo=timezone(timedelta(hours=8)))
    for item in ExportXmlParser().get_full_data_in_dict():
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


class HeartRateGetter:
    def __init__(self, file_path):
        self.file_path = file_path
        self.time = get_workout_time(self.file_path)
        self.heartrate_list = get_heartrate_list(self.time)
        pass
