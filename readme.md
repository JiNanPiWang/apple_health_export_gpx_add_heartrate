## 中文版（[English version](#English)）：(Project not finished)
#### 使用方法
1. 将苹果健康的数据导出并解压，可以得到一个文件夹名叫`导出`
2. 将导出文件夹中的apple_health_export复制到根目录中
3. 将apple_health_export中的 导出.xml 重命名为export.xml



#### 起因：

使用苹果健康导出的gpx文件，不包含心率信息，但实际上如果使用的是苹果手表记录活动，在/apple_health_export/导出.xml中包含了手表记录的心率信息。

#### 作用：

本程序的目的是将心率信息加入至导出的gpx文件中，并可以上传至其他平台，如strava等。

------

衷心感谢yihong0618的项目[[running_page](https://github.com/yihong0618/running_page)]

没有running_page，我就不会开始这个项目。


## English:
#### How to use
1. Export and unzip the Apple Health data, and you will get a folder named Export.
2. Copy apple_health_export in the export folder to the root directory
3. Rename export(in your language).xml in apple_health_export to export.xml



#### cause:

The gpx file exported using Apple Health does not contain heart rate information. However, if an Apple Watch is actually used to record activities, /apple_health_export/export.xml contains the heart rate information recorded by the watch.

#### What the program does:

The purpose of this program is to add heart rate information to the exported gpx file and upload it to other platforms such as strava.

------

Thanks to yihong0618's project [[running_page](https://github.com/yihong0618/running_page)]

Without running_page, I would not have started this project.