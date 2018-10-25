from graphics import *
import math, time
import random


#定义画骰子点的函数
def draw_circle(position_x, position_y, radius, win):
    cir = Circle(Point(position_x, position_y), radius)
    cir.setFill('black')
    cir.draw(win)

    
#定义全部掷骰子函数
def roll_all(roll_point, pause_point, Dice1, Dice2, Dice3, Dice4, Dice5,win):

    while True:
        cli = win.checkMouse()  #检测鼠标点击事件
        #如果点击暂停按钮则停止改变
        if cli and cli.getX() > pause_point.getX() and cli.getX(
        ) < pause_point.getX() + 40 and cli.getY() > pause_point.getY(
        ) and cli.getY() < pause_point.getX() + 40:
            break
        Dice1.roll_number_one()
        Dice2.roll_number_one()
        Dice3.roll_number_one()
        Dice4.roll_number_one()
        Dice5.roll_number_one()


#定义骰子类
class Dice:
    dice_number = 1  #骰子的点数

    def __init__(self, position_x, position_y, win,
                 point):  #骰子的初始化参数，位置横纵坐标和点数以及窗口,暂停按钮的位置
        self.position_x = position_x
        self.position_y = position_y
        self.win = win
        self.point = point

        #建立对象时运行这两个函数，画出骰子
        self.draw_dice()
        self.draw_number(1)

    def draw_dice(self):  #画一个边长为80的正方形作为骰子以及一个按钮
        Dice = Rectangle(
            Point(self.position_x, self.position_y),
            Point(self.position_x + 80, self.position_y + 80))
        Dice.setFill('white')
        Dice.draw(self.win)

        roll_button = Rectangle(
            Point(self.position_x, self.position_y - 40),
            Point(self.position_x + 80, self.position_y - 10))
        roll_button.setFill('grey')
        roll_button.draw(self.win)
        Text(Point(self.position_x + 40, self.position_y - 25),
             "die").draw(self.win)
        print(__name__)

    def draw_number(self, number):  #画骰子里的点数
        #点数为1,5时画中间的一点
        if number in [1, 3, 5]:
            draw_circle(self.position_x + 35, self.position_y + 35, 5,
                        self.win)

        #点数为2,3,5,6时画左下角的点
        if number in [2, 4, 3, 5, 6]:
            draw_circle(self.position_x + 15, self.position_y + 15, 5,
                        self.win)

        #点数为6时画左边中间的点
        if number in [6]:
            draw_circle(self.position_x + 15, self.position_y + 35, 5,
                        self.win)

        #点数为4,5,6时画左边上面的点
        if number in [4, 5, 6]:
            draw_circle(self.position_x + 55, self.position_y + 15, 5,
                        self.win)

        #点数为2,3,5,6时画右边边上面的点
        if number in [2, 3, 4, 5, 6]:
            draw_circle(self.position_x + 55, self.position_y + 55, 5,
                        self.win)

        #点数为4,6时画右边中间的点
        if number in [6]:
            draw_circle(self.position_x + 55, self.position_y + 35, 5,
                        self.win)

        #点数为4，5,6时画右边下面的点
        if number in [4, 5, 6]:
            draw_circle(self.position_x + 15, self.position_y + 55, 5,
                        self.win)

    #一直反复roll点的函数
    def roll_number(self):
        while True:
            cli = self.win.checkMouse()  #检测鼠标点击事件
            if cli:  #如果点击暂停按钮则停止改变
                if cli.getX() > self.point.getX() and cli.getX(
                ) < self.point.getX() + 40 and cli.getY() > self.point.getY(
                ) and cli.getY() < self.point.getX() + 40:
                    break
            roll_random = random.randint(1, 6)  #生成随机点数

            self.dice_number = roll_random  #记录点数

            print(roll_random)
            self.draw_dice()
            self.draw_number(roll_random)
            time.sleep(0.1)

    #只roll一次点的函数
    def roll_number_one(self):

        roll_random = random.randint(1, 6)  #生成随机点数

        self.dice_number = roll_random  #记录点数

        print(roll_random)
        self.draw_dice()
        self.draw_number(roll_random)
        time.sleep(0.1)

    #判断按钮点击事件
    def roll_click(self, cli):
        if (cli.getX() > self.position_x and cli.getX() < self.position_x + 80
                and cli.getY() > self.position_y - 40
                and cli.getY() < self.position_y - 10):
            self.roll_number()
            return 1
        return 0

    #返回骰子的当前点数
    def getDiceNumber(self):
        return self.dice_number
        # self.draw_number(roll_random)

