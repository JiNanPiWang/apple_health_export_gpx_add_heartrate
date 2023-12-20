## 中文版（[English version](#English)）：
#### 使用方法（最好使用Python3.9+）
1. 将苹果健康的数据导出并解压，可以得到一个文件夹名叫导出
2. 将导出文件夹中的apple_health_export复制到根目录中
3. 将apple_health_export中的 导出.xml 重命名为export.xml

#### 如果想自动上传到strava，需要补充config中的strava_api.json文件，内容如下：
```json
{
    "client_id": "strava的client_id",
    "client_secret": "strava的client_secret",
    "refresh_token": "strava的refresh_token",
    "activity_type": "运动类型，如run, bike, hike等"
}
```

#### 起因：

使用苹果健康导出的gpx文件，不包含心率信息，但实际上如果使用的是苹果手表记录活动，在/apple_health_export/导出.xml中包含了手表记录的心率信息。

#### 作用：

本程序的目的是将心率信息加入至导出的gpx文件中，并可以上传至其他平台，如strava等。

------

衷心感谢yihong0618的项目[[running_page](https://github.com/yihong0618/running_page)]

没有running_page，我就不会开始这个项目。

常见gpx格式解读：
```xml
<trkpt lat="***" lon="***">  <!--  经纬度   -->
 <ele>53.4</ele>  <!--  海拔   -->
 <time>2023-11-12T06:50:58Z</time>  <!--  UTC时间   -->
 <extensions>  <!--  扩展的内容   -->
  <gpxtpx:TrackPointExtension>  <!--  轨迹点扩展   -->
   <gpxtpx:atemp>12</gpxtpx:atemp>  <!--  温度   -->
   <gpxtpx:hr>110</gpxtpx:hr>  <!--  心率   -->
   <gpxtpx:cad>26</gpxtpx:cad>  <!--  踏频   -->
  </gpxtpx:TrackPointExtension>
 </extensions>
</trkpt>
```
苹果健康运动记录gpx格式解读：
```xml
<trkpt lon="***" lat="***">  <!--  经纬度   -->
    <ele>19.396494</ele>  <!--  海拔   -->
    <time>2019-10-03T08:02:18Z</time>  <!--  UTC时间   -->
    <extensions>
        <speed>1.500479</speed>  <!--  速度   -->
        <course>139.218750</course>  <!--  轨迹点的方向   -->
        <hAcc>2.281494</hAcc>  <!--  水平精度   -->
        <vAcc>1.575096</vAcc>  <!--  垂直精度   -->
    </extensions>
</trkpt>
```


## English:
#### How to use(It is best to use Python3.9+)
1. Export and unzip the Apple Health data, and you will get a folder named Export.
2. Copy apple_health_export in the export folder to the root directory
3. Rename export(in your language).xml in apple_health_export to export.xml

#### If you want to automatically upload to strava, you need to add the strava_api.json file in the config, the content is as follows:
```json
{
     "client_id": "client_id of strava",
     "client_secret": "strava's client_secret",
     "refresh_token": "strava's refresh_token",
     "activity_type": "Sports type, such as run, bike, hike, etc."
}
```

#### cause:

The gpx file exported using Apple Health does not contain heart rate information. However, if an Apple Watch is actually used to record activities, /apple_health_export/export.xml contains the heart rate information recorded by the watch.

#### What the program does:

The purpose of this program is to add heart rate information to the exported gpx file and upload it to other platforms such as strava.

------

Thanks to yihong0618's project [[running_page](https://github.com/yihong0618/running_page)]

Without running_page, I would not have started this project.

Common GPX Format:
```xml
<trkpt lat="***" lon="***">  <!--  Latitude and Longitude   -->
 <ele>53.4</ele>  <!--  Elevation   -->
 <time>2023-11-12T06:50:58Z</time>  <!--  UTC Time   -->
 <extensions>  <!--  Extended Information   -->
  <gpxtpx:TrackPointExtension>  <!--  Track Point Extension   -->
   <gpxtpx:atemp>12</gpxtpx:atemp>  <!--  Temperature   -->
   <gpxtpx:hr>110</gpxtpx:hr>  <!--  Heart Rate   -->
   <gpxtpx:cad>26</gpxtpx:cad>  <!--  Cadence   -->
  </gpxtpx:TrackPointExtension>
 </extensions>
</trkpt>
```

Apple Health Fitness GPX Format:
```xml
<trkpt lon="***" lat="***">  <!--  Longitude and Latitude   -->
    <ele>19.396494</ele>  <!--  Elevation   -->
    <time>2019-10-03T08:02:18Z</time>  <!--  UTC Time   -->
    <extensions>
        <speed>1.500479</speed>  <!--  Speed   -->
        <course>139.218750</course>  <!--  Course (Direction of the track point)   -->
        <hAcc>2.281494</hAcc>  <!--  Horizontal Accuracy   -->
        <vAcc>1.575096</vAcc>  <!--  Vertical Accuracy   -->
    </extensions>
</trkpt>
```