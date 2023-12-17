import gpxpy
from src.workout_gpx_parser import WorkoutGpxParser

if __name__ == '__main__':
    gpx_file = open('apple_health_export/workout-routes/route_2023-10-18_9.30pm.gpx', 'r')

    gpx = gpxpy.parse(gpx_file)

    for track in gpx.tracks:
        for segment in track.segments:
            for point in segment.points:
                print(point.name)