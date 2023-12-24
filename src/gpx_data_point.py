# workout_gpx_parser.py

# 一条（一秒）的gpx数据
# single(one second) gpx data

from datetime import datetime, timezone, timedelta


class GpxDataPoint:
    def __init__(self, lon=None, lat=None, ele=None, time=None, speed=None, atemp=None, hr=None, cad=None):
        self.lon = lon

        self.lat = lat
        self.ele = ele
        self.time = time
        self.speed = speed
        self.atemp = atemp  # temperature
        self.hr = hr  # heart rate
        self.cad = cad  # cadence

        # 解析日期时间字符串
        self.datetime_origin = self.parse_datetime(time) if time else None

        # 转换到UTC+0时区
        self.datetime_utc0 = self.convert_to_utc0(self.datetime_origin) if self.datetime_origin else None

        # 提取日期和时间部分
        self.date_part = self.datetime_utc0.strftime("%Y-%m-%d") if self.datetime_utc0 else None
        self.time_part = self.datetime_utc0.strftime("%H:%M:%S") if self.datetime_utc0 else None

    def __str__(self):
        return (f"Lon: {self.lon}, \
                 Lat: {self.lat}, \
                 Elevation: {self.ele}, \
                 Time: {self.time}, \
                 Speed: {self.speed}, \
                 Temperature: {self.speed}, \
                 Heart rate: {self.speed}, \
                 Cadence: {self.speed}, \
                 Time: {self.time}, \
                 Time_utc0: {self.datetime_utc0}\n\n"
                )

    def __getitem__(self, item):
        return getattr(self, item)

    @staticmethod
    def parse_datetime(time_string):
        try:
            return datetime.strptime(time_string, "%Y-%m-%dT%H:%M:%SZ")
        except ValueError:
            try:
                # 尝试解析另一种格式
                # 这种%z就是时区的意思，%z是+0800，%Z是CST
                return datetime.strptime(time_string, "%Y-%m-%d %H:%M:%S %z")
            except ValueError:
                try:
                    # 尝试解析类似 2019-10-23_9.24pm 的格式
                    return datetime.strptime(time_string, "%Y-%m-%d_%I.%M%p")
                except ValueError:
                    # 如果三种格式都无法解析，返回 None
                    return None

    @staticmethod
    def convert_to_utc0(dt):
        if dt:
            # 转换到UTC+0时区
            if dt.tzinfo:
                dt_utc0 = dt.astimezone(timezone.utc)
                return dt_utc0
            else:
                return dt.replace(tzinfo=timezone.utc)
        return None
