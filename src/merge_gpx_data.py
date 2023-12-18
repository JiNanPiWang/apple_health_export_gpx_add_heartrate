# merge_gpx_data.py
# merge single_gpx_data.py's data

import os
from .config import WORKOUT_ROUTES_WITH_HR


class MergeGpxData:
    def __init__(self, file_name: str, content: str):
        self.file_path = os.path.join(WORKOUT_ROUTES_WITH_HR, f'{file_name}_new.gpx')
        self.content = content

        if not os.path.exists(WORKOUT_ROUTES_WITH_HR):
            os.mkdir(WORKOUT_ROUTES_WITH_HR)

    def save_gpx(self):
        with open(self.file_path, 'w') as f:
            f.write(self.content)

