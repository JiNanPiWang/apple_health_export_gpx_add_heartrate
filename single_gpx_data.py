# workout_gpx_parser.py

# 一条（一秒）的gpx数据
# single(one second) gpx data

from datetime import datetime, timezone, timedelta


class SingleGpxData:
    def __init__(self, lon=None, lat=None, ele=None, time=None, speed=None, atemp=None, hr=None, cad=None):
        self.lon = lon
        self.lat = lat
        if __name__ == '__main__':
            self.ele = ele
        self.time = time
        self.speed = speed
        self.atemp = atemp  # temperature
        self.hr = hr  # heart rate
        self.cad = cad  # cadence

        # 解析日期时间字符串
        self.datetime = datetime.strptime(time, "%Y-%m-%dT%H:%M:%SZ") if time else None
        self.date_part = self.datetime.strftime("%Y-%m-%d") if self.datetime else None
        self.time_part = self.datetime.strftime("%H:%M:%S") if self.datetime else None

    def __str__(self):
        return f"Lon: {self.lon}, \
                 Lat: {self.lat}, \
                 Elevation: {self.ele}, \
                 Time: {self.time}, \
                 Speed: {self.speed}, \
                 Temperature: {self.speed}, \
                 Heart rate: {self.speed}, \
                 Cadence: {self.speed}"