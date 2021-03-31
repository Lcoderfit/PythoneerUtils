# CreateQrCode使用文档
## 一、目录结构
### 1.1 导出目录

* 在PythonUtils目录下打开终端，使用 tree /F /A CreateQrCode 即可显示CreateQrCode中的目录结构， /F表示显示每个文件夹中文件的名称；/A表示使用Ascii字符进行编码

* 将目录结构导出到文件,如果不加/A参数会乱码：tree /F /A CreateQrCode > result.txt

```txt
CreateQrCode                    生成个性二维码的实用工具
|   create_qrcode.py            对MyQR库进行封装，用于生成个性二维码
|   flask_api.py                定义了一个简易的api，可以通过传入source和content参数来控制生成的二维码的内容及视觉效果
|   nohup.out                   nohup命令生成的日志文件
|   qrcode_nginx.conf           nginx的配置文件
|   README-CreateQrCode.md      说明文档
|   requirements-linux.txt      linux环境下运行所需要下载的包
|   requirements-windows.txt    windows下运行所需要的包
|   __init__.py
|   
+---dst                         生成的目标二维码保存的路径
|                               dst.gif 生成的目标二维码,支持生成.png/.jpg/.gif格式的二维码
|       
+---source
|       source.gif              用于渲染二维码的文件,必须是.png/.jpg/.gif格式
|       
\---__pycache__
        create_qrcode.cpython-38.pyc
```

## 二、功能介绍
### 2.1.生成个性二维码

#### 2.1.1 请求格式

| URL          | /qr_code            |
| ------------ | ------------------- |
| 支持格式     | multipart/form-data |
| HTTP请求方法 | POST                |
| 是否登入验证 | 否                  |
| 请求数限制   | 无                  |
#### 2.1.2 请求参数

| 名称    | 类型   | 是否必选 | 示例值                                                       | 描述                                                         |
| ------- | ------ | -------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| source  | file   | 否       | case1：source.gif<br>case2： source.png<br>case3：source.jpg | 如果不传入该参数，则默认生成黑白二维码；<br>如果传入该参数，则必须为.gif/.png/.jpg格式的文件，用于渲染二维码背景;<br>如果传入.gif格式文件，则生成.gif格式的动态二维码，<br>传入.png/.jpg格式的图片均会生成.png格式的二维码 |
| content | string | 是       | "http://blessing.lcoderfit.com"                              | 需要存储在二维码中的信息                                     |

#### 2.1.3 返回结果

| 名称     | 类型   | 示例值                          | 描述                                                         |
| -------- | ------ | ------------------------------- | ------------------------------------------------------------ |
| filename | string | "dst.png"                       | 返回的二维码文件名称                                         |
| img      | string | "iVBORw0KGgoAAAANSUhEUgAA....." | 二维码字节流经过base64编码之后得到新的字节流，然后再经过ascii进行解码会得到一串字符串 |

#### 2.1.4 接口调用结果示例

##### 2.1.4.1 调用成功

* 状态码：HTTP/1.1 200 OK
* 响应体
```json
{
    "code": "ok",
    "message": {
        "filename": "dst.png",
        "img": "iVBORw0KGgoAAAANSUhEUgAAAU0AAAFNAQAAAACsiwBpAAACX0lEQVR4nO2bQY6jMBBFXwUksnPf\nAG5Cz8mgb0ZuQm4AuyABfxZ2QndGM+oNNEPsTST7Lb4o2fWr7Jj45hhO3yUhohGNaEQj+t+hvflR\n9OfJLMycgEtYqPej9ahoJklqYMi05GerySXdZ3ai9XBo6n+mFKpfOE0GgBMycaF/w+Y1BUT0CfW7\noNTVUnu2q3vTemBUanA3FFLA9gJeE00k1UA2mPHxTn/G7wInzVsIeHl0MDOz8OVNHwWZL4avZuY9\n0m60Hg5FX8cYpjNJVJ9Xbj+u9dDokIKvAlKganB9CrJ34JEUdqL1cCiS1IGJSuqycPI7jSCpJRvD\nTom7YN3SbJTJrHB9aqJq6L0pvZTqH+50J1oPig7ZDJQXO08nZFXrpCkk6CQ6onVRfxBlvguR65bM\n4fwJfQkXZuJBtBp6zwX+5HfBEeUdAFWTdyTBGsUQbGBKm7zLRhOQd5meRwzB6iGgUutCLHDLlw9m\nKYZgVbS3FGRWMKRgdakOf3FwfdtEQETJRplJLSDfIzJfrBX9eRMBER1Sk8zK6xlQHdasLpdibTda\nD4d+MqWV1GWj6YsphWhKV0ZDCEZ/TQBYyMJJCEE2xnS8LvrcKdUMlC2PrtESlB/XemT08wuKRHAp\nIJkMLgUxF2yD3l9QuD69L0wnoGyDTV1bwCujSy6ganLdCJ2K27079yiT40G0EZrMWE3eMSWCsnV9\nqnhxuTn68X61czKj+lJe3fgvdB0Br4UudYFv0/nkm3f3y7KO2CNaGV2a1Sz3Bc1yTXAv1mIIVkP/\neDP31xH/4hHRiEY0okdFfwPlfuOlz0ln7gAAAABJRU5ErkJggg==\n"
    }
}
```

##### 2.1.4.2 调用失败

* 状态码：HTTP/1.1 200 OK
* 响应体

```json
{
    "code": "error",
    "message": "xxxxxx"
}
```

## 三、启动项目

### 3.1 windows下启动-仅用于本地调试

#### 3.1.1 windows下创建虚拟环境

* 在PythoneerUtils目录下打开终端, 输入如下命令，-m表示mode，python -m venv表示使用python的创建虚拟环境的模式，第二个venv可以随意命名，表示生成的虚拟环境文件名，python -m venv venv会在当前目录下生成一个venv的文件，创建一个名为venv的虚拟环境

  ```shell script
  $python -m venv venv
  ```

* 启动虚拟环境

  ```shell script
  $venv\Scripts\activate
  ```

* 退出虚拟环境

  ```shell script
  $deactivate
  ```

* 删除虚拟环境

  ```text
  直接删除之前创建的虚拟环境文件即可
  $rd /s venv  # 会弹出是否删除venv文件的提示，输入Y然后回车即可
  
  rd /s/q dirname # 表示强制删除文件夹及其中的子目录和文件，不会弹出提示
  在cmd中使用help rd查看详情
  ```

#### 3.1.2 pip下载依赖模块

* 创建并启动虚拟环境之后，需要下载项目中的依赖模块，CreateQrCode中有一个requirements-windows.txt文件，该文件是通过

  ```shell script
  pip freeze > requirements-windows.txt
  ```

  命令生成的，里面包含了项目所需要依赖包对应的版本信息，切换到CreateQrCode目录下，使用如下命令下载requirements-windows.txt中涉及到的依赖包

  ```shell script
  pip install -r requirements-windows.txt
  ```

* 如果下载包的过程中报错，则应查看是在下载哪个包的时候报错了，可以手动下载该包：

  ```text
  方法1：pip install -U package_name #下载最新版本的包
  方法2：pip install -U package_name==1.0.0 #下载该包的1.0.0版本(版本号根据实际情况更改)
  ```

* 注意：有的时候我们会在虚拟环境内更新pip版本，可能会遇到在虚拟环境内更新pip（python -m pip install -U pip）报错的情况：
  
```text
  ceback (most recent call last):
    File "/home/PushProject/CreateQrCode/venv/bin/pip", line 7, in <module>
      from pip._internal.cli.main import main
  File "/home/PushProject/CreateQrCode/venv/lib/python3.5/site-packages/pip/_internal/cli/main.py", line 60
      sys.stderr.write(f"ERROR: {exc}")
```

  如果遇到该问题，可以先回退到原始版本：例如原始版本是19.0，则：

  ```shell script
python -m pip install -U pip==19.0
  ```

  然后通过pip来更新pip自身的版本：

  ```text
  pip install -U pip # 更新到pip最新版本
  或指定版本更新：pip install -U pip==20.2.3
  pip -V # 查看当前的pip版本
  ```


* 题外话

  ```text
  1.查看windows下pip源
  在C:\Users\Lcoderfit\pip目录下打开cmd，然后type pip.ini就会显示相关内容
  
  2.查看Linux的pip源
  cat ~/.pip/pip.conf
  ```

#### 3.1.3 启动项目

* 在CreateQrCode目录下输入如下命令启动服务，然后使用postman或者apipost等工具，根据第二节中的请求格式跟请求参数对

  <http://localhost:8062/qr_code>发送POST请求即可

  ```shell script
  $python flask_api.py
  ```

### 3.2 Linux下启动-可用于生产环境部署

#### 3.2.1 Linux下创建虚拟环境

* 首先将PythonUtils目录整个迁移到自己的Linux服务器上，python3创建虚拟环境可能需要下载python3-venv包

  ```shell script
  $sudo apt-get install python3-venv
  ```

* 创建虚拟环境，与windows下命令相同：

  ```shell script
  $python -m venv venv
  ```

* 激活虚拟环境

  ```shell script
  $source venv/bin/activate
  ```

* 退出虚拟环境

  ```shell script
  $deactivate
  ```

* 虚拟环境（手动删除虚拟环境文件即可）

   ```shell script
  rm venv
  ```

#### 3.2.2 pip下载依赖包

* 相关信息可以参考3.1.2, 命令与windows下相同

  ```shell script
  pip install -r requirements-linux.txt
  ```

#### 3.2.3 设置nginx配置文件

* 参考CreateQrCode/qrcode_nginx.conf，可以根据自己实际情况将8062端口号改成其他端口，如果你租的是阿里云，需要在阿里云控制台设置相应端口的

  ```text
  # 通过nginx默认端口接口接收请求，然后将请求转发到8062端口给flask_api.py程序进行处理
  server {
      listen       80; # nginx默认端口，无需修改
      server_name  xxx.xxxx.xxx; # 配置自己租的域名，这样可以直接对该域名发送请求
  
      charset utf-8;
      access_log  /home/PushProject/CreateQrCode/nginx.log; # 生成nginx日志的路径，这里可以根据自己实际情况来配置
  
      # 允许客户端发送的请求实体的最大值
      client_max_body_size 10m; # nginx允许客户端发送的请求实体的最大值默认为1MB；这里设置为10MB，因为POST请求上传的文件可能会比较大。
  
      location / {
          try_files /_not_exists_ @backend;
      }
  
      location @backend {
          proxy_set_header X-Forwarded-For $remote_addr;
          proxy_set_header Host            $http_host;
  
          proxy_pass http://127.0.0.1:8062;
      }
  }
  ```

* 注意，当你用apipost或者postman等工具发送post请求之后，如果显示：

  ```text
  “413 Request Entity Too Large”
  ```

  响应时，是由于nginx默认的request body为1M，如果你上传的文件超过1M，则会报该错误。

* 将配置链接到nginx

  ```shell script
  $sudo ln -s /path/to/your/qrcode_nginx.conf /etc/nginx/sites-enabled/
  ```

* 启动nginx

  ```shell script
  $/etc/init.d/nginx start
  ```

* 启动nginx之后，如果又修改了qrcode_nginx.conf,则只需要重新载入即可

  ```shell script
  $/etc/init.d/nginx reload
  ```

* 启动程序

  ```shell script
  $nohup python flask_api.py &
  ```

  如果只改了程序没改qrcode_nginx.conf，则杀掉进程之后更新代码再重启程序即可，不需要重载nginx

  ```text
  $ps aux|grep flask_api # 找到flask_api对应的进程号(PID)
  $kill -9 PID
  修改完程序之后重启：
  $nohup python flask_api.py &
  ```

## 四、知识点回顾
### 4.1 为什么图片要进行base64编码
* 首先，base64准确来说是编码，不是加密。减少http请求数（但是并不一定能提高性能，下文会讲），网页上的每一个图片，都需要消耗一个http请求来下载，如果把图片进行base64编码转为字符串，可以随html页面一起下载下来，减少http请求次数

* 可以起到一定程度的保密性，别人没办法一眼看出照片内容

* 将一些二进制字符转换成普通字符用于网络传输，一些二进制字符在传输协议中属于控制字符，不能直接传送需要转换一下

  ```text
  //在css里的写法
  #fkbx-spch, #fkbx-hspch {
    background: url(data:image/gif;base64,R0lGODlhHAAmAKIHAKqqqsvLy0hISObm5vf394uLiwAAAP///yH5B…EoqQqJKAIBaQOVKHAXr3t7txgBjboSvB8EpLoFZywOAo3LFE5lYs/QW9LT1TRk1V7S2xYJADs=) no-repeat center;
  }
  
  //在html代码img标签里的写法
  <img src="data:image/gif;base64,R0lGODlhHAAmAKIHAKqqqsvLy0hISObm5vf394uLiwAAAP///yH5B…EoqQqJKAIBaQOVKHAXr3t7txgBjboSvB8EpLoFZywOAo3LFE5lYs/QW9LT1TRk1V7S2xYJADs=">
  ```
### 4.2 base64对图片进行编码一定能提高性能吗？

* 不一定，base64虽然能减少http请求次数，但是会导致css或html文件体积的增大（一般经过base64编码之后的图片内容比之前大1/3），从而导致CRP阻塞（critical rendering path，关键渲染路径），CRP指的是浏览器从接收到服务器的HTML响应开始到屏幕显示出整个页面的过程
* HTML和CSS会阻塞渲染，但是图片不会（因为图片是用额外的http进行请求）
* 如果将base64编码值放到CSS里，则页面解析CSS生成CSSOM的时间会增加（首先解析HTML，在head标签中遇到link标签会下载对应的css文件，然后生成CSSOM，CSSOM未生成之前所有东西都不会展示）
* 如果图片经常改动，则维护代码会更加困难，因为需要手动修改这些经过base64编码的值

### 4.3 什么情况下用base64？

* 图片比较小，经过base64编码后也不会大很多
* 图片不会经常更新，在整个网址中复用性很高（因为图片改动之后base64编码也变了）
* continue

### 4.4 如何解决base64的问题，有没有其他方案——CssSprites

* CssSprites也可以减少http请求次数，它是将页面中许多小图合成一个大图，这样本来10个图片需要10个http请求，合成一个大图之后就只需要一个
* 降低因图片更新导致的代码维护难度
* 不会增加CSS体积，不会导致CRP阻塞
* continue

### 4.5 CssSprites的缺点

* 开发和维护都比较麻烦，如果背景又少许改动则合并图也需要做改动。
* continue

### 4.6 base64编码的具体过程



### 4.7 什么是关键渲染路径？

