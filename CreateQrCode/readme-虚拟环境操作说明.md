1.用python3创建虚拟环境需要下载python3-venv
sudo apt-get install python3-venv
2.创建虚拟环境, -m表示模式，python -m venv表示使用python的操作虚拟环境的模式，python -m venv venv在当前目录下创建一个venv的目录，在该venv目录下创建虚拟环境
python -m venv venv
3.激活虚拟环境
source venv/bin/activate
4.退出虚拟环境
deactivate
5.删除虚拟环境（手动删除虚拟环境文件即可）
rm venv
6.导出requestments.txt
pip freeze > requestments.txt
7.根据requestments.txt安装包
pip install -r requestments.txt

8.查看Linux的pip源
cat ~/.pip/pip.conf

9.查windows的pip源
在C:\Users\Lcoderfit\pip目录下打开cmd，然后type pip.ini就会显示相关内容

10.python更新pip
python -m pip install -U pip
注意：这个一般在全局环境下更新pip之后可以正常使用pip命令，但是如果在虚拟环境下更新后使用pip命令可能会报错：
ceback (most recent call last):
  File "/home/PushProject/CreateQrCode/venv/bin/pip", line 7, in <module>
    from pip._internal.cli.main import main
  File "/home/PushProject/CreateQrCode/venv/lib/python3.5/site-packages/pip/_internal/cli/main.py", line 60
    sys.stderr.write(f"ERROR: {exc}")

解决办法：
先通过全局更新pip版本，然后pip -V查看pip的最新版本号，例如：20.3.4
然后通过pip显式安装：pip install -U pip==20.3.4

11.pip更新pip
pip install -U pip==20.3.4

12.安装特定版本的包
pip install -U package_name==版本号

13.服务器启动时候ip使用:0.0.0.0，lsof -i命令会显示其地址为: *:端口号

14.如果只改了程序没改nginx conf，则杀点进程之后更新代码再重启程序即可，不需要重新reload nginx

15.当发送请求之后收到“413 Request Entity Too Large”响应时，是由于nginx默认的request body为1M，如果你上传的文件超过1M，则会报该错误。
解决办法：
在nginx的server选项中添加client_max_body_size配置，例如：

server {
    listen       80;
    server_name  code.lcoderfit.com;

    # 表示允许客户端发送的请求实体的最大值
    client_max_body_size 10m;
}

16.Content-Type的单位是字节