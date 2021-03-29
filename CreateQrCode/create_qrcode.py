# 如果太久没有了需要先更新pip，然后更新MyQR和numpy版本
# python -m pip install -U pip
# pip install -U MyQR       pip install -U numpy
import os
import re

from MyQR import myqr


class GenerateCode:
    """生成各种码(二维码、条形码等)"""

    def __init__(self):
        """初始化函数"""
        # 生成的二维码默认保存在当前工作目录下的dst目录下
        self.dst_dir = os.path.join(os.getcwd(), "dst")
        # 默认生成的二维码名称为当前时间（不带后缀名的部分）
        # self.dst_name = datetime.datetime.now().strftime("%Y%m%d%H%M%S%f")
        self.dst_name = "dst"

    def qr_code(self, words: str, source=None, dst_name=None):
        """生成二维码，支持jpg,png,gif等多种格式

        :param words: 需要存入二维码中的内容
        :param source: 用于和二维码合成的照片的路径，没有可设置为None
        :param dst_name: 最后生成的二维码文件名
        :return:
        """
        if not words or not isinstance(words, str):
            raise Exception("content must be a not empty string")
        # 判断源文件名是否合法, source如果存在则必须是一个字符串
        if source and (not isinstance(source, str)
                       or not re.search(r"(.jpg|.png|.gif)$", source) or not os.path.isfile(source)):
            raise Exception("source is not valid file")

        # dst_name不需要带有后缀
        if dst_name and isinstance(dst_name, str):
            dst_name = dst_name.split(".")[0]
        else:
            dst_name = self.dst_name

        # 如果不需要使用source渲染二维码，则直接使用默认生成黑白二维码
        if not source:
            suffix = "png"
        else:
            # 获取源文件名后缀, 生成的文件后缀应与源文件名后缀一致
            suffix = source.split(".")[-1]
        dst_name += "." + suffix
        # 生成的目标文件的绝对路径
        dst = os.path.join(self.dst_dir, dst_name)

        # 如果文件已存在则删除该文件，os.path.exists会判断目录或文件是否存在
        if os.path.exists(dst):
            os.remove(dst)

        # 生成二维码
        result = myqr.run(
            words=words,  # 扫码后显示的内容或网站
            version=1,  # 照片的宽度，从1~40
            level="Q",  # 容错水平，('L', 'M', 'Q', 'H')等级逐渐提高
            picture=source,
            colorized=True,  # 由黑白变为彩色
            contrast=1.5,  # 用以调节图片的对比度，1.0 表示原始图片，更小的值表示更低对比度，更大反之。默认为1.0。
            brightness=1.6,  # 用来调节图片的亮度，其余用法和取值与 -con 相同
            save_dir=self.dst_dir,  # 生成的二维码保存的路径
            save_name=dst_name,
        )
        # result值示例：(3, 'Q', 'E:\\SocialProject\\Utils-Tags\\CreateQrCode\\dst\\des.gif')
        # result[2]表示生成的目标二维码的保存路径及文件名
        return result[2]


if __name__ == '__main__':
    # 二维码携带的信息，如果要使扫码后跳转到网页，则需要包含http/https前缀，否则只会显示文字内容
    content = "http://blessing.lcoderfit.com"
    # 获取当前工作目录
    base_path = os.getcwd()
    filename = 'source.gif'
    # os.path.normpath()：将路径变成标准路径
    # str.replace("\\", "/")：将windows路径分隔符"\\"替换为通用分隔符"/"
    source_file_path = os.path.normpath(os.path.join(base_path, filename))
    save_dir = os.path.normpath(base_path)
    save_name = "dst.gif"

    generator = GenerateCode()
    generator.qr_code(content, source_file_path)
    # generator.qr_code(content, source_file_path, save_name)
