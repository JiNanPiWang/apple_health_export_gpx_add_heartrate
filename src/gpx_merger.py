# gpx_merger.py
# merge gpx_data_point.py's data
# once only merge to one gpx file

import os
import random

import gpxpy
import json

from config.paths import WORKOUT_ROUTES_WITH_HR
from .gpx_data_point import GpxDataPoint
from .workout_gpx_parser import WorkoutGpxParser
import xml.etree.ElementTree as ET
from .heart_rate_getter import HeartRateGetter


class GpxMerger:
    def __init__(self, file: str):
        self.file = file
        self.new_file_path = os.path.join(WORKOUT_ROUTES_WITH_HR, f'{file[:-4]}_new.gpx')
        self.gpx = gpxpy.gpx.GPX()
        self.content = None

        if not os.path.exists(WORKOUT_ROUTES_WITH_HR):
            os.mkdir(WORKOUT_ROUTES_WITH_HR)

    def merge_points(self):
        self.gpx.nsmap["gpxtpx"] = "http://www.garmin.com/xmlschemas/TrackPointExtension/v1"
        gpx_track = gpxpy.gpx.GPXTrack()
        gpx_track.name = "gpx from Apple health export"
        gpx_track.type = "cycling"
        self.gpx.tracks.append(gpx_track)

        # Create first segment in our GPX track:
        # 类似gpx有gpx_track的属性，gpx_track又包括gpx_segment这个属性，gpx_segment包含points的属性，points由轨迹点组成
        # 所以最后还是轨迹点
        gpx_segment = gpxpy.gpx.GPXTrackSegment()
        gpx_track.segments.append(gpx_segment)

        workout_data = WorkoutGpxParser(self.file)

        # 心率获取
        heart_rate_getter = HeartRateGetter(None, self.file)
        # 时间是键，心率是值
        heart_rate_dict = heart_rate_getter.heartrate_dict

        for data in workout_data.get_full_data_in_dict():
            data_trans = GpxDataPoint(lon=data["lon"], lat=data["lat"], time=data["time"], ele=data["ele"])
            point = gpxpy.gpx.GPXTrackPoint(
                latitude=data_trans.lat,
                longitude=data_trans.lon,
                time=data_trans.datetime_utc0,
                elevation=data_trans.ele
            )

            # 心率目前默认取下一个时间的心率值
            gpx_extension_hr = ET.fromstring(
                f"""<gpxtpx:TrackPointExtension xmlns:gpxtpx="http://www.garmin.com/xmlschemas/TrackPointExtension/v1">
                    <gpxtpx:hr>{heart_rate_dict[point.time]}</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                    """
            )
            point.extensions.append(gpx_extension_hr)
            gpx_segment.points.append(point)

        self.content = self.gpx.to_xml()

    def save_gpx(self):
        if self.content is None:
            raise ValueError("gpx is None, you need to merge points[merge_points()] first")
        with open(self.new_file_path, 'w') as f:
            f.write(self.content)
            print(f'{self.file} successfully processed and saved.')
