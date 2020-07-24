import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

import turtle
import turtle as T
import random
import time

# 画樱花的躯干(60,t)

def Tree(branch, t):
    time.sleep(0.05)
    T.speed(50)
    if branch > 3:
        if 8 <= branch <= 12:
            if random.randint(0, 2) == 0:
                t.color('snow')  # 白
            else:
                t.color('lightcoral')  # 淡珊瑚色
            t.pensize(branch / 3)
        elif branch < 8:
            if random.randint(0, 1) == 0:
                t.color('snow')
            else:
                t.color('yellow')  # 淡珊瑚色
            t.pensize(branch / 2)
        else:
            t.color('sienna')  # 赭(zhě)色
            t.pensize(branch / 10)  # 6
        t.forward(branch)
        a = 1.5 * random.random()
        t.right(20 * a)
        b = 1.5 * random.random()
        Tree(branch - 10 * b, t)
        t.left(40 * a)
        Tree(branch - 10 * b, t)
        t.right(20 * a)
        t.up()
        t.backward(branch)
        t.down()

# 掉落的花瓣
def Petal(m, t):
    for i in range(m):
        a = 200 - 400 * random.random()
        b = 10 - 20 * random.random()
        t.up()
        t.forward(b)
        t.left(90)
        t.forward(a)
        t.down()
        t.color('lightcoral')  # 淡珊瑚色
        t.circle(1)
        t.up()
        t.backward(a)
        t.right(90)
        t.backward(b)

# 绘图区域
t = T.Turtle()
# 画布大小
w = T.Screen()
t.hideturtle()  # 隐藏画笔
t.getscreen().tracer(5, 0)
w.screensize(bg='black')  # wheat小麦
t.left(90)
t.up()
t.backward(150)
t.down()
t.color('sienna')

# 画樱花的躯干
Tree(60, t)
# 掉落的花瓣
Petal(120, t)


t = turtle.Turtle()
def fd(a):
    t.forward(a)
t.pensize(3)
t.hideturtle()
t.speed(100)
def up():
    t.penup()
def down():
    t.pendown()
t.hideturtle()
t.speed(100)
t.fillcolor('red')
up()
t.goto(-300,-300)
down()
t.pencolor('yellow')
t.write('祝****小可爱： ',font=('Courier',30,'bold'))
up()

up()
t.goto(10,-300)
down()
t.pencolor('red')
t.write('*节日快乐~*\n*开开心心~*',font=("Courier",30,'bold'))

def snow(snow_count):
    t.hideturtle()
    t.speed(1000)
    t.pensize(2)
    for i in range(snow_count):
        r = random.random()
        g = random.random()
        b = random.random()
        t.pencolor(r, g, b)
        t.pu()
        t.goto(random.randint(-350, 350), random.randint(1, 270))
        t.pd()
        dens = random.randint(8, 12)
        snowsize = random.randint(10, 14)
        for _ in range(dens):
            t.forward(snowsize)  # 向当前画笔方向移动snowsize像素长度
            t.backward(snowsize)  # 向当前画笔相反方向移动snowsize像素长度
            t.right(360 / dens)  # 顺时针移动360 / dens度

def main():
    #t.setup(800, 600, 0, 0)
            # p.tracer(False)
    #t.bgcolor("black")
    snow(50)
    #ground(30)
            # p.tracer(True)
    #t.mainloop()
main()


turtle.penup()
turtle.left(180)
turtle.fd(300)
turtle.pendown()
turtle.right(90)

# 花蕊
turtle.fillcolor("red")
turtle.begin_fill()
turtle.circle(10, 100)
turtle.circle(25, 110)
turtle.left(50)
turtle.circle(60, 45)
turtle.circle(20, 170)
turtle.right(24)
turtle.fd(30)
turtle.left(10)
turtle.circle(30, 110)
turtle.fd(20)
turtle.left(40)
turtle.circle(90, 70)
turtle.circle(30, 150)
turtle.right(30)
turtle.fd(15)
turtle.circle(80, 90)
turtle.left(15)
turtle.fd(45)
turtle.right(165)
turtle.fd(20)
turtle.left(155)
turtle.circle(150, 80)
turtle.left(50)
turtle.circle(150, 90)
turtle.end_fill()

# 花瓣1
turtle.left(150)
turtle.circle(-90, 70)
turtle.left(20)
turtle.circle(75, 105)
turtle.setheading(60)
turtle.circle(80, 98)
turtle.circle(-90, 40)

# 花瓣2
turtle.left(180)
turtle.circle(90, 40)
turtle.circle(-80, 98)
turtle.setheading(-83)

# 叶子1
turtle.fd(30)
turtle.left(90)
turtle.fd(25)
turtle.left(45)
turtle.fillcolor("green")
turtle.begin_fill()
turtle.circle(-80, 90)
turtle.right(90)
turtle.circle(-80, 90)
turtle.end_fill()

turtle.right(135)
turtle.fd(60)
turtle.left(180)
turtle.fd(85)
turtle.left(90)
turtle.fd(80)

# 叶子2
turtle.right(90)
turtle.right(45)
turtle.fillcolor("green")
turtle.begin_fill()
turtle.circle(80, 90)
turtle.left(90)
turtle.circle(80, 90)
turtle.end_fill()

turtle.left(135)
turtle.fd(60)
turtle.left(180)
turtle.fd(60)
turtle.right(90)
turtle.circle(200, 60)
time.sleep(10)
#w.exitonclick()