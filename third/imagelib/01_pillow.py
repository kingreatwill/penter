# python -m pip install --upgrade Pillow
# http://www.lenna.org/
# http://www.lenna.org/full/l_hires.jpg

"""
try:
    with Image.open(infile) as im:
        print(infile, im.format, "%dx%d" % im.size, im.mode)
except IOError:
    pass
"""

from PIL import Image

im = Image.open("lenna.jpg")
print(im.format, im.size, im.mode)
# im.show()
#  im.save(outfile) # 可以改变文件格式

# 剪切
box = (100, 100, 200, 200)
region = im.crop(box)
# region.show()
# 粘贴
im.paste(region, (150, 150, 250, 250))
#im.paste((256,256,0),(0,0,100,100))  ##(256,256,0)表示黄色

# im.show()

def roll(image, delta):
    """Roll an image sideways."""
    xsize, ysize = image.size

    delta = delta % xsize
    if delta == 0: return image

    part1 = image.crop((0, 0, delta, ysize))
    part2 = image.crop((delta, 0, xsize, ysize))
    image.paste(part1, (xsize - delta, 0, xsize, ysize))
    image.paste(part2, (0, 0, xsize - delta, ysize))

    return image


# roll(im, 100).show()

out1 = im.resize((128, 128))
out2_1 = im.rotate(30, Image.NEAREST,1)

# im.rotate(45)                             #逆时针旋转 45 度角。
# im.transpose(Image.FLIP_LEFT_RIGHT)       #左右对换。
# im.transpose(Image.FLIP_TOP_BOTTOM)       #上下对换。
# im.transpose(Image.ROTATE_90)             #旋转 90 度角。
# im.transpose(Image.ROTATE_180)            #旋转 180 度角。
# im.transpose(Image.ROTATE_270)            #旋转 270 度角。

from PIL import ImageFilter  ## 调取ImageFilter
# imgF = Image.open("E:\mywife.jpg")
# bluF = imgF.filter(ImageFilter.BLUR)                ##均值滤波
# conF = imgF.filter(ImageFilter.CONTOUR)             ##找轮廓
# edgeF = imgF.filter(ImageFilter.FIND_EDGES)         ##边缘检测
# #模糊滤波
# img_blur = img.filter(ImageFilter.BLUR)
# #轮廓滤波
# img_contour = img.filter(ImageFilter.CONTOUR)
# #细节滤波
# img_detail = img.filter(ImageFilter.DETAIL)
# #边界增强滤波
# img_edge_enhance = img.filter(ImageFilter.EDGE_ENHANCE)
# #锐化滤波
# img_sharp = img.filter(ImageFilter.SHARPEN)
# #高斯模糊滤波
# img_gauss = img.filter(ImageFilter.GaussianBlur(radius=2))  # radius指定平滑半径，也就是模糊的程度。

# im.filter(ImageFilter.CONTOUR).show()


from PIL import ImageEnhance

# PIL的ImageEnhance类专门用于图像增强处理，可以增强（减弱）图像的亮度、对比度、色度、以及锐度。
#
# 亮度（Brightness），色度（Color），对比度（Contrast），锐度（Sharpness）
# # 原始图像
# img = Image.open('image.jpg')
# # 亮度增强
# img_bright = ImageEnhance.Brightness(imag).enhance(3)
# image_bright.show()
# # 色度增强
# img_color = ImageEnhance.Color(img).enhance(2)
# image_color.show()
# # 对比度增强
# img_contrast = ImageEnhance.Contrast(img).enhance(3)
# image_contrast.show()
# # 锐度增强
# img_sharp = ImageEnhance.Sharpness(img).enhance(2)
# image_sharp.show()


"""
图像的模式，常见的mode 有 “L” (luminance) 表示灰度图像，“RGB”表示真彩色图像，和 “CMYK” 表示出版图像，表明图像所使用像素格式。如下表为常见的nodes描述：

modes	描述
1	1位像素，黑和白，存成8位的像素
L	8位像素，黑白
P	8位像素，使用调色板映射到任何其他模式
RGB	3× 8位像素，真彩
RGBA	4×8位像素，真彩+透明通道
CMYK	4×8位像素，颜色隔离
YCbCr	3×8位像素，彩色视频格式
I	32位整型像素
F	32位浮点型像素
"""

im2 = Image.open("wallhaven-nmekwy.jpg")
print(im2.format)
print(im2.getbbox())

# im2.convert('L').show() # 黑白
# im2.convert('1').show() # 图像二值化

# Image.new("RGB", (128, 128), "#FF0000").show()
# Image.new("RGB", (128, 128)).show()
# Image.new("RGB", (128, 128), "green").show()

# im2.copy()

# 混合
# Image.blend(image1,image2, alpha)

# 值越大 im2越明显
# Image.blend(im, im2.resize((400, 274)), 0.2).show()
# Image.blend(im, im2.resize((400, 274)), 0.8).show()


# 拆分出（红，绿，蓝）三个通道的图像
r, g, b = im.split()
r2, g2, b2 = im2.split()
# b2.show()

# 复合类使用给定的两张图像及mask图像作为透明度，插值出一张新的图像
# Image.composite(im, im2.resize((400, 274)),b2.resize((400, 274))).show()


# Image.eval(im2, lambda x:x*2.0).show()

# 合并类使用一些单通道图像，创建一个新的图像。变量bands为一个图像的元组或者列表，每个通道的模式由变量mode描述。所有通道必须有相同的尺寸。
# Image.merge("RGB",[r2.resize((400, 274)),g,b]).show()

sequ = im.getdata()
sequ0 = list(sequ)
# print(sequ0)

# 最大值 最小值
print(im.getextrema())

# 多通道返回（rgb）
print(im.getpixel((0,0)))
# 单通道的返回一个值
print(b.getpixel((0,0)))



im_gif = Image.open("gg.gif")
# im_gif.show() # 第0帧
# im_gif.seek(25)
# im_gif.show() # 第25帧
# print(im_gif.tell()) #返回当前帧所处位置 25

# 在原图上缩小
# im.thumbnail((100,100))
# im.show()

# 使用给定的尺寸生成一张新的图像，与原图有相同的模式，使用给定的转换方式将原图数据拷贝到新的图像中。
# 在当前的PIL版本中，参数method为EXTENT（裁剪出一个矩形区域），AFFINE（仿射变换），QUAD（将正方形转换为矩形），MESH（一个操作映射多个正方形）或者PERSPECTIVE。
# 变量filter定义了对原始图像中像素的滤波器。
# 在当前的版本中，变量filter为NEAREST、BILINEAR、BICUBIC或者ANTIALIAS之一。
# 如果忽略，或者图像模式为“1”或者“P”，该变量设置为NEAREST。
# im.transform((400, 400), Image.EXTENT, (0, 0, 500, 500)).show()
# im2.transform((400, 400), Image.EXTENT, (0, 0, 500, 500)).show()
#im.transform((400, 400), Image.AFFINE, (1,2,3,2,1,4)).show()
#im.transform((200, 200), Image.QUAD, (0, 0, 0, 500, 600, 500, 600, 0)).show()
#im.transform((200, 200), Image.PERSPECTIVE, (1, 2, 3, 2, 1, 6, 1, 2)).show()



im.close()
im2.close()
