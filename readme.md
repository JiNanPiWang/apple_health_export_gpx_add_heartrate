## 中文版（[English version](#English)）：

### 使用方法

#### 1. 将苹果健康的数据导出，可参考[百度经验](https://jingyan.baidu.com/article/e9fb46e167cc6b3421f766e1.html)，并发送到您的电脑上，解压后可以得到一个文件夹名叫`导出`

#### 2. 将导出文件夹中的apple_health_export复制到本项目的根目录中

#### 3. 将apple_health_export中的 导出.xml 重命名为export.xml

#### 4. 如果您需要将导出的内容自动上传到strava，请进行以下操作：

4.1 创建你自己的strava应用，进入[Strava API](https://www.strava.com/settings/api)
创建应用，创建完毕后你可以看到`客户 ID`和`客户端密钥`这两个内容

4.2 运行`python3 utils/strava_local_client.py get_write_token <client_id> <client_secret>`，
其中，将<client_id>替换为你看到的`客户 ID`，<client_secret>替换为`客户端密钥`

4.3
运行后，你会在终端看到一个网址，打开它，登录你的strava账号，然后会跳转到一个网页，
网页中会有一行内容，复制这个网页中的那一行内容，然后粘贴到本项目的config/strava_config.json
中的`access_token`中

#### 5. 运行`python3 main.py`，即可得到加入了心率的gpx文件，如果您想要将生成文件的上传到您的strava账户，请您运行`python3 main.py --upload-to-strava`

### 起因：

苹果手表过去的运动记录不能自动传到strava，即使使用苹果健康导出了gpx文件，但其中也不包含心率信息，
但实际上如果使用的是苹果手表记录活动，在/apple_health_export/导出.xml中包含了手表记录的
心率信息。

### 作用：

本程序的目的是将心率信息加入至导出的gpx文件中，并可以自动上传至strava。

------

衷心感谢yihong0618的项目[[running_page](https://github.com/yihong0618/running_page)]
和barrald的项目[[strava-uploader](https://github.com/barrald/strava-uploader)]

没有running_page，我就不会开始这个项目。没有strava-uploader，这里也不会有自动上传到strava的功能。

## English:

### Instructions

#### 1. To export Apple Health data, please refer to [Baidu Experience](https://jingyan.baidu.com/article/e9fb46e167cc6b3421f766e1.html) and send it to your computer. After decompression, you can get a The folder name is `Export`

#### 2. Copy apple_health_export in the export folder to the root directory of this project

#### 3. Rename export.xml in apple_health_export to export.xml

#### 4. If you need to automatically upload the exported content to strava, please do the following:

4.1 Create your own strava application and enter [Strava API](https://www.strava.com/settings/api)
Create the application. After creation, you can see the two contents `Customer ID` and `Client Key`

4.2 Run `python3 utils/strava_local_client.py get_write_token <client_id> <client_secret>`,
Among them, replace <client_id> with the `client ID` you see, and replace <client_secret> with `client secret`

4.3
After running, you will see a URL in the terminal, open it, log in to your strava account, and then jump to a web page,
There will be a line of content in the web page. Copy that line of content in the web page and paste it into the config/strava_config.json of this project.
`access_token` in

#### 5. Run `python3 main.py` to get the gpx file with heart rate added. If you want to upload the generated file to your strava account, please run `python3 main.py --upload -to-strava`

### Cause:

Past exercise records from Apple Watch cannot be automatically transferred to Strava. Even if a gpx file is exported using Apple Health, it does not contain heart rate information.
But in fact, if you use an Apple watch to record activities, /apple_health_export/export.xml contains the information recorded by the watch.
Heart rate information.

### Function:

The purpose of this program is to add heart rate information to the exported gpx file and automatically upload it to strava.

------

Sincere thanks to yihong0618 for his project [[running_page](https://github.com/yihong0618/running_page)]
and barrald's project [[strava-uploader](https://github.com/barrald/strava-uploader)]

I wouldn't have started this project without running_page. Without strava-uploader, there will be no automatic upload to strava function.
