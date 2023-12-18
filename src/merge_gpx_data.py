# merge_gpx_data.py
# merge single_gpx_data.py's data

import os
from .config import WORKOUT_ROUTES_WITH_HR


class MergeGpxData:
    def __init__(self, file_name):
        self.file_path = os.path.join(WORKOUT_ROUTES_WITH_HR, f'{file_name}_new.gpx')
        if not os.path.exists(WORKOUT_ROUTES_WITH_HR):
            os.mkdir(WORKOUT_ROUTES_WITH_HR)

    def save_gpx(self):
        with open(self.file_path, 'w') as f:
            f.write(
                """
                <?xml version="1.0" encoding="UTF-8"?>
<gpx creator="StravaGPX" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.topografix.com/GPX/1/1 http://www.topografix.com/GPX/1/1/gpx.xsd http://www.garmin.com/xmlschemas/GpxExtensions/v3 http://www.garmin.com/xmlschemas/GpxExtensionsv3.xsd http://www.garmin.com/xmlschemas/TrackPointExtension/v1 http://www.garmin.com/xmlschemas/TrackPointExtensionv1.xsd" version="1.1" xmlns="http://www.topografix.com/GPX/1/1" xmlns:gpxtpx="http://www.garmin.com/xmlschemas/TrackPointExtension/v1" xmlns:gpxx="http://www.garmin.com/xmlschemas/GpxExtensions/v3">
                """
            )
