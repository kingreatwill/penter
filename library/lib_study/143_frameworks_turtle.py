# turtle 海龟  海龟绘图很适合用来引导孩子学习编程。 最初来自于 Wally Feurzeig, Seymour Papert 和 Cynthia Solomon 于 1967 年所创造的 Logo 编程语言。
# import turtle
# turtle.forward(150) # 它将(在屏幕上)朝所面对的 x 轴正方向前进 150 像素
# turtle.right(25) # 原地右转 25 度

# https://docs.python.org/zh-cn/3/library/turtle.html
from turtle import *
color('red', 'yellow')
begin_fill()
while True:
    forward(200)
    left(170)
    if abs(pos()) < 1:
        break
end_fill()
done()


import time
time.sleep(30)