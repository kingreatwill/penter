#!/usr/bin/python
# _*_ coding:utf-8 _*_

__author__ = 'Svend'
# pip3 install pillow
from PIL import Image
import argparse


class Ascii:
    def __init__(self):
        width, height, input_file, out_file = self.parse_args()
        self.input_file_name = input_file
        self.out_file_name = out_file
        self.img_width = width
        self.img_height = height

    def get_char(self, r, g, b, alpha=256):
        """
        rbg 转字符
        :param r:
        :param g:
        :param b:
        :param alpha:
        :return:
        """
        if alpha == 0:
            return ' '
        gary = (2126 * r + 7152 * g + 722 * b) / 10000
        ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")
        # gary / 256 = x / len(ascii_char)
        x = int(gary / (alpha + 1.0) * len(ascii_char))
        return ascii_char[x]

    def write_file(self, content):
        """
        写入转换过后的字符画到文件
        :param content: 转换过后的字符画
        :return:
        """
        with open(self.out_file_name, 'w') as f:
            f.write(content)

    def parse_args(self):
        """
        参数解析
        """
        parser = argparse.ArgumentParser()
        parser.add_argument('input_file')
        parser.add_argument('out_file')
        parser.add_argument('--width', type=int, default=50)
        parser.add_argument('--height', type=int, default=50)

        args = parser.parse_args()
        img_width, img_height, input_file_name, out_file_name = \
            args.width, args.height, args.input_file, args.out_file

        return img_width, img_height, input_file_name, out_file_name

    def run(self):
        """
        Ascii 类的主函数
        :return:
        """
        im = Image.open(self.input_file_name)
        im = im.resize((self.img_width, self.img_height), Image.NEAREST)
        txt = ''
        for i in range(self.img_height):
            for j in range(self.img_width):
                content = im.getpixel((j, i))
                if isinstance(content, int):
                    content = (content, content, content)
                txt += self.get_char(*content)
            txt += '\n'
        print(txt)
        self.write_file(txt)


if __name__ == '__main__':
    Ascii().run()