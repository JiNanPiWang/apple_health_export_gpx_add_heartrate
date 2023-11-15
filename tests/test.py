from workout_gpx_parser import WorkoutGpxParser


if __name__ == '__main__':
    parser = WorkoutGpxParser('route_2019-10-03_8.53am.gpx')
    for data_point in parser.parse_heart_rate_data():
        lon, lat, ele, time, speed = data_point
        # 在这里执行你的处理逻辑，例如打印或保存数据
        print(f'Lon: {lon}, Lat: {lat}, Elevation: {ele}, Time: {time}, Speed: {speed}')
