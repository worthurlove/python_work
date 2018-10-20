#Fuction:simulate the flight of a cannonball
#Author:worthurlove
#Date:2018.10.20

from graphics import *
import math,time
import numpy as np

win = GraphWin("加农炮", 1400, 600)  #载入界面，标题栏
win.setCoords(0.0, 0.0, 1400, 600)  #按比例转换坐标

# 绘制接口
Text(Point(50, 550), "初始速度:").draw(win)  #初始速度
Text(Point(50, 450), "高度:").draw(win)  #炮弹初始高度
Text(Point(50, 350), "发射角度:").draw(win)  #炮弹发射角度
'''
分别为速度，高度和角度输入框
'''
input_v = Entry(Point(50, 500), 10)  #速度输入框
input_v.setText("100")
input_v.draw(win)

input_h = Entry(Point(50, 400), 10)  #高度输入框
input_h.setText("0")
input_h.draw(win)

input_a = Entry(Point(50, 300), 10)  #角度输入框
input_a.setText("45")
input_a.draw(win)

button = Text(Point(50, 100), "发射")  #按钮字样
button.draw(win)
Rectangle(Point(25, 75), Point(75, 125)).draw(win)  #长方形按钮

Line(Point(125,50),Point(1400,50)).draw(win)#横坐标线
Line(Point(125,50),Point(125,600)).draw(win)#竖坐标线

#定义运动轨迹函数
def flying(v,h,a,win):
    x = 100 #起飞水平点
    y = h   #起飞高度

    v_forward = v*math.cos(math.radians(a))#水平初始速度
    v_up = v*math.sin(math.radians(a))#垂直初始速度

    highest = 0
    for t in np.arange(0,100,0.1):#将最高点标记为红色
        if v_up - 9.8*t <= 0 and highest == 0:
            cir = Circle(Point(x,y),4)
            cir.draw(win)
            cir.setFill('red')
            highest = 1

        cir = Circle(Point(x,y),2)
        cir.draw(win)#在窗口画轨迹点

        x = 125 + v_forward*t#水平距离变化
        y = 50 + h + v_up*t - 0.5*9.8*t**2#垂直距离变化
        if y < 50:
            break
        time.sleep(0.1)


running = 1
while running:#窗口主循环
    cor = win.getMouse()
    if (cor.getX() > 25.0) and (cor.getX() < 75.0):#判断按钮点击事件
        #分别获取输入的速度，高度和角度
        v = float(input_v.getText())
        h = float(input_h.getText())
        a = float(input_a.getText())
        
        button.setText('已起飞')
        flying(v,h,a,win)
    
