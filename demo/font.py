from fontTools.ttLib import TTFont

font = TTFont('i.jzj9999.com.ttf') # 打开本地的ttf文件
font.saveXML('i.jzj9999.com.xml')  # 转换成xml
