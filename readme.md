## 中文版（[English version](#English)）：(Project not finished)

#### 使用方法

##### 1. 将苹果健康的数据导出，可参考[百度经验](https://jingyan.baidu.com/article/e9fb46e167cc6b3421f766e1.html)，并发送到您的电脑上，解压后可以得到一个文件夹名叫`导出`

##### 2. 将导出文件夹中的apple_health_export复制到本项目的根目录中

##### 3. 将apple_health_export中的 导出.xml 重命名为export.xml

##### 4. 如果您需要将导出的内容自动上传到strava，请进行以下操作：

4.1 创建你自己的strava应用，进入[Strava API](https://www.strava.com/settings/api)
创建应用，创建完毕后你可以看到`客户 ID`和`客户端密钥`这两个内容

4.2 运行`python3 utils/strava_local_client.py get_write_token <client_id> <client_secret>`，
其中，将<client_id>替换为你看到的`客户 ID`，<client_secret>替换为`客户端密钥`

4.3
运行后，你会在终端看到一个网址，打开它，登录你的strava账号，然后会跳转到一个网页，
网页中会有一行内容，复制这个网页中的那一行内容，然后粘贴到本项目的config/strava_config.json
中的`access_token`中

##### 5. 运行`python3 main.py`，即可得到加入了心率的gpx文件，如果您想要将生成文件的上传到您的strava账户，请您运行`python3 main.py --upload-to-strava`

#### 起因：

苹果手表过去的运动记录不能自动传到strava，即使使用苹果健康导出了gpx文件，但其中也不包含心率信息，
但实际上如果使用的是苹果手表记录活动，在/apple_health_export/导出.xml中包含了手表记录的
心率信息。

#### 作用：

本程序的目的是将心率信息加入至导出的gpx文件中，并可以自动上传至strava。

------

衷心感谢yihong0618的项目[[running_page](https://github.com/yihong0618/running_page)]
和barrald的项目[[strava-uploader](https://github.com/barrald/strava-uploader)]

没有running_page，我就不会开始这个项目。没有strava-uploader，这里也不会有自动上传到strava的功能。

## English:

#### How to use

1. Export and unzip the Apple Health data, and you will get a folder named Export.
2. Copy apple_health_export in the export folder to the root directory
3. Rename export(in your language).xml in apple_health_export to export.xml

#### cause:

The gpx file exported using Apple Health does not contain heart rate information. However, if an Apple Watch is actually
used to record activities, /apple_health_export/export.xml contains the heart rate information recorded by the watch.

#### What the program does:

The purpose of this program is to add heart rate information to the exported gpx file and upload it to other platforms
such as strava.

------

Thanks to yihong0618's project [[running_page](https://github.com/yihong0618/running_page)]

Without running_page, I would not have started this project.