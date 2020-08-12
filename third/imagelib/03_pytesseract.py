# https://github.com/madmaze/pytesseract
# 验证码识别
# 下载tesseract最新版：https://digi.bib.uni-mannheim.de/tesseract/
# https://tesseract-ocr.github.io/tessdoc/4.0-with-LSTM.html#400-alpha-for-windows
# https://www.dropbox.com/s/obiqvrt4m53pmoz/tesseract-4.0.0-alpha.zip?dl=1
# https://github.com/manisandro/gImageReader/releases/download/v3.2.1/gImageReader_3.2.1_qt5_x86_64_tesseract4.0.0.git2f10be5.exe
# E:\bigdata\ai\tesseract-4.0.0-alpha
# 下载训练数据 https://tesseract-ocr.github.io/tessdoc/Data-Files.html
# 拷贝文件到E:\bigdata\ai\tesseract-4.0.0-alpha\tessdata文件夹
# pip install pytesseract
from PIL import Image

import pytesseract

# If you don't have tesseract executable in your PATH, include the following:
pytesseract.pytesseract.tesseract_cmd = r'E:\bigdata\ai\tesseract-4.0.0-alpha\tesseract.exe'
# Example tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract'

# Simple image to string
print(pytesseract.image_to_string(Image.open('test.png')))

print(pytesseract.image_to_string(Image.open('m.jpg')))

# chi_tra 繁体
print(pytesseract.image_to_string(Image.open('zh-cn.png'), lang='chi_sim'))
