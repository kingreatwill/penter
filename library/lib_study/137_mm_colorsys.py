# http://poynton.ca/ColorFAQ.html
# https://www.cambridgeincolour.com/tutorials/color-spaces.htm
# 颜色空间(HSV/HSB与HLS)的区别 https://blog.csdn.net/u010712012/article/details/85240100
"""
YIQ，是NTSC（National Television Standards Committee）电视系统标准。
Y是提供黑白电视及彩色电视的亮度信号（Luminance），即亮度（Brightness），
I代表In-phase，色彩从橙色到青色，
Q代表Quadrature-phase，色彩从紫色到黄绿色。

colorsys.rgb_to_yiq(r, g, b)
把颜色从RGB值转为YIQ值。

colorsys.yiq_to_rgb(y, i, q)
把颜色从YIQ值转为RGB值。


HLS 是Hue(色相)、Luminance(亮度)、Saturation(饱和度)
colorsys.rgb_to_hls(r, g, b)
把颜色从RGB值转为HLS值。

colorsys.hls_to_rgb(h, l, s)
把颜色从HLS值转为RGB值。
"""

"""
# HSV(Hue, Saturation, Value)是根据颜色的直观特性由A. R. Smith在1978年创建的一种颜色空间, 也称六角锥体模型(Hexcone Model)。
色调H
用角度度量，取值范围为0°～360°，从红色开始按逆时针方向计算，红色为0°，绿色为120°,蓝色为240°。它们的补色是：黄色为60°，青色为180°,紫色为300°；
饱和度S
饱和度S表示颜色接近光谱色的程度。一种颜色，可以看成是某种光谱色与白色混合的结果。其中光谱色所占的比例愈大，颜色接近光谱色的程度就愈高，颜色的饱和度也就愈高。饱和度高，颜色则深而艳。
光谱色的白光成分为0，饱和度达到最高。通常取值范围为0%～100%，值越大，颜色越饱和。
明度V
明度表示颜色明亮的程度，对于光源色，明度值与发光体的光亮度有关；对于物体色，此值和物体的透射比或反射比有关。通常取值范围为0%（黑）到100%（白）。
RGB和CMY颜色模型都是面向硬件的，而HSV（Hue Saturation Value）颜色模型是面向用户的。
HSV模型的三维表示从RGB立方体演化而来。设想从RGB沿立方体对角线的白色顶点向黑色顶点观察，就可以看到立方体的六边形外形。六边形边界表示色彩，水平轴表示纯度，明度沿垂直轴测量。

colorsys.rgb_to_hsv(r, g, b)
把颜色从RGB值转为HSV值。

colorsys.hsv_to_rgb(h, s, v)
把颜色从HSV值转为RGB值。
"""
import colorsys

print(colorsys.rgb_to_hsv(0.2, 0.4, 0.4))

print(colorsys.hsv_to_rgb(0.5, 0.5, 0.4))

