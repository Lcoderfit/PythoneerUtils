import os

from flask import Flask, request, send_from_directory, make_response, jsonify
from typing import List
from create_qrcode import GenerateCode

app = Flask("GenerateQrCodeApi")


@app.route("/qr_code", methods=['POST'])
def get_qr_code():
    """获取二维码"""
    # 获取multipart/form-data方式上传的text对象
    content = request.values.get("content")
    # 获取multipart/form-data方式上传的file对象
    # 用get方式获取，如果请求中不含有source字段，则默认为None
    file = request.files.get("source")

    if file:
        if file.filename.endswith(".jpg"):
            filename = file.filename.split(".")[0] + ".png"
        else:
            filename = file.filename
        source_path = os.path.join(os.getcwd(), "source", filename)
        # 如果source_path中某一级的目录不存在，则会报错
        file.save(source_path)
    else:
        source_path = None

    # 生成二维码，获取生成的二维码的绝对路径, 当source_path为None时，则默认生成黑白二维码
    # multipart/form-data方式发送请求，可以同时发送file和text类型的字段，并且一些字段为空一些字段有值也是允许的
    dst_path = generator.qr_code(content, source_path)

    # 获取文件所在目录及文件名
    dst_dir = os.path.dirname(dst_path)
    dst_name = os.path.split(dst_path)[-1]

    # 发送文件流到前端
    try:
        # as_attachment=True表示设置响应头中 "Content-Disposition: attachment"
        # 用于控制文件的下载方式，Content-Disposition: attachment弹出对话框让用户下载
        # Content-Disposition: inline表示在页面内打开文件内容
        response = make_response(
            send_from_directory(dst_dir, dst_name, as_attachment=True)
        )
        return response
    except Exception as e:
        return jsonify({"code": "error", "message": "{}".format(e)})


if __name__ == '__main__':
    generator = GenerateCode()
    app.run("0.0.0.0", port=8062)
