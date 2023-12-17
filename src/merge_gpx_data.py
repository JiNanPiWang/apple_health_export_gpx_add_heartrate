# merge_gpx_data.py
# merge single_gpx_data.py's data

import os


class MergeGpxData:
    def __init__(self, file_name):
        # 当前路径
        self.path = os.path.dirname(__file__)
        # 获取项目根目录
        self.project_root = os.path.abspath(os.path.join(self.path, '..'))
        
        self.file_name = file_name