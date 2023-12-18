import os

import gpxpy
from src.workout_gpx_parser import WorkoutGpxParser
from src.single_gpx_data import SingleGpxData
from src.merge_gpx_data import MergeGpxData
from src.config import PROJECT_ROOT, WORKOUT_ROUTES
import xml.etree.ElementTree as ET


if __name__ == '__main__':
    files = os.listdir(WORKOUT_ROUTES)

    # 打印所有文件名
    for gpx_file in files:
        print(gpx_file)

        gpx = gpxpy.gpx.GPX()
        gpx.nsmap["gpxtpx"] = "http://www.garmin.com/xmlschemas/TrackPointExtension/v1"
        gpx_track = gpxpy.gpx.GPXTrack()
        gpx_track.name = "gpx from Apple health export"
        gpx_track.type = "cycling"
        gpx.tracks.append(gpx_track)

        # Create first segment in our GPX track:
        # 类似gpx有gpx_track的属性，gpx_track又包括gpx_segment这个属性，gpx_segment包含points的属性，points由轨迹点组成
        # 所以最后还是轨迹点
        gpx_segment = gpxpy.gpx.GPXTrackSegment()
        gpx_track.segments.append(gpx_segment)

        workout_data = WorkoutGpxParser(gpx_file)
        for data in workout_data.get_full_data_in_dict():
            data_trans = SingleGpxData(lon=data["lon"], lat=data["lat"], time=data["time"], ele=data["ele"])
            point = gpxpy.gpx.GPXTrackPoint(
                latitude=data_trans.lat,
                longitude=data_trans.lon,
                time=data_trans.datetime_utc0,
                elevation=data_trans.ele
            )
            gpx_extension_hr = ET.fromstring(
                f"""<gpxtpx:TrackPointExtension xmlns:gpxtpx="http://www.garmin.com/xmlschemas/TrackPointExtension/v1">
                    <gpxtpx:hr>{60}</gpxtpx:hr>
                    </gpxtpx:TrackPointExtension>
                    """
            )
            point.extensions.append(gpx_extension_hr)
            gpx_segment.points.append(point)

            merge_gpx = MergeGpxData(gpx_file[:-4], gpx.to_xml())
            merge_gpx.save_gpx()

        break
