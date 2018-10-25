#Function:一个叫做dice pocker 的小游戏
#Author:worthurlove
#Date:2018.10.22
'''
游戏规则：
1.The player starts with $100. 
2.Each round costs $10,subtracted from the player's money at the start.
3.All five dice are rolled randomly .
4.The player gets two chances to enhance the hand by rerolling some or all of the dice. 
5.At the end of the hand, the player's money is updated.

界面要求：
1.The current score is displayed. 
2.Automatically terminates when the player goes broke.
3.Choose to quit at appropriate points.
4.Present visual cues:what is going on?What the valid user responses are?

结算规则：
1.两个一对 
2.三个一样的
3.一对加上三个一样的
4.四个一样的
5.一条龙（1-5或者2-6）
6.5个一样的
'''

from graphics import *
import myclass
import random, math, time
import numpy as np


win = GraphWin("Dice Poker", 800, 600)  #载入界面，标题栏
win.setCoords(0.0, 0.0, 800, 600)  #按比例转换坐标
win.setBackground('green')

money = 100  #初始赌注

rounds = 0  #记录游戏轮数

result_number = [0] * 6  #记录三次投掷之后的骰子点数

#画出暂停按钮
pause_point = Point(700, 100)
pause_button = Rectangle(
    pause_point, Point(pause_point.getX() + 60,pause_point.getY() + 40))
pause_button.setFill('grey')
pause_button.draw(win)
Text(Point(pause_point.getX() + 30, pause_point.getY() + 20), "quit").draw(win)

#画出roll所有骰子的按钮
roll_point = Point(250, 250)
roll_all_button = Rectangle(
    roll_point, Point(roll_point.getX() + 300,
                      roll_point.getY() + 40))
roll_all_button.setFill('grey')
roll_all_button.draw(win)
Text(Point(roll_point.getX() + 150,
           roll_point.getY() + 20), "roll all").draw(win)

#画出得分文字
score_point = Point(350, 180)
score_button = Rectangle(
    score_point, Point(score_point.getX() + 100,
                       score_point.getY() + 40))
score_button.setFill('grey')
score_button.draw(win)
Text(Point(score_point.getX() + 50,
           score_point.getY() + 20), "score").draw(win)

#显示奖励结果
score = Text(Point(score_point.getX() + 50, score_point.getY() - 40), "奖励：$0")
score.draw(win)

#显示进行了多少轮游戏
game_times = Text(Point(400, 580), '')
game_times.setText('you have played ' + str(rounds) + ' rounds of games')
game_times.setTextColor('red')
game_times.setSize(20)
game_times.draw(win)

#x显示剩余赌注
total_money = Text(Point(400, 520), '')
total_money.setText('Now,you have $' + str(money))
total_money.setTextColor('red')
total_money.setSize(30)
total_money.draw(win)

#创建5个骰子实例对象
dice1 = myclass.Dice(100, 400, win, pause_point)
dice2 = myclass.Dice(220, 400, win, pause_point)
dice3 = myclass.Dice(340, 400, win, pause_point)
dice4 = myclass.Dice(460, 400, win, pause_point)
dice5 = myclass.Dice(580, 400, win, pause_point)

#游戏的整个过程
while money > 10:  #赌注大于$10继续游戏
    money -= 10  #每局下注$10
    rounds = rounds + 1  #游戏轮数加1

    #首先roll所有骰子的点
    while True:
        cli = win.getMouse()
        if (cli.getX() > roll_point.getX()
                and cli.getX() < roll_point.getX() + 300
                and cli.getY() > roll_point.getY()
                and cli.getY() < roll_point.getY() + 40):
            #判断rollall按钮点击事件
            myclass.roll_all(roll_point, pause_point, dice1, dice2, dice3, dice4,dice5,win)
            break

    #然后又两次机会roll五个骰子中的一个
    for i in range(2):
        while True:
            cli = win.getMouse()
            if dice1.roll_click(cli) == 1 or dice2.roll_click(
                    cli) == 1 or dice3.roll_click(
                        cli) == 1 or dice4.roll_click(
                            cli) == 1 or dice5.roll_click(cli) == 1:
                break

    #计算结果
    result_number[0] = dice1.getDiceNumber()
    result_number[1] = dice2.getDiceNumber()
    result_number[2] = dice3.getDiceNumber()
    result_number[3] = dice4.getDiceNumber()
    result_number[4] = dice5.getDiceNumber()
    '''
    七种可能的情况
    '''
    kinds = [0] * 7
    for i in range(5):
        kinds[result_number[i]] += 1

    #情况1：5个一样的
    if 5 in kinds:
        money += 30
        score.setText('Five of a kind 奖励：$30')

    #计算情况2：四个一样的
    elif 4 in kinds:
        money += 15
        score.setText('Four of a kind 奖励：$15')

    #情况3：三个一样的和一对
    elif (3 in kinds) and (2 in kinds):
        money += 12
        score.setText('Full house 奖励：$12')

    #情况4：三个一样的
    elif 3 in kinds:
        money += 8
        score.setText('Three of a kind 奖励：$8')

    #情况5：一条龙（1-5或者2-6）
    elif not (2 in kinds) and (kinds[0] == 0 or kinds[6] == 0):
        money += 20
        score.setText('Straight 奖励：$20')
    #情况6：两个一对
    elif kinds.count(2) == 2:
        money += 5
        score.setText('Two pairs 奖励：$5')
    #情况7：垃圾
    else:
        score.setText('gabage：$0')


    #信息更新
    game_times.setText(
        'you have played ' + str(rounds) + ' rounds of games')  #游戏轮数显示
    total_money.setText('Now,you have $' + str(money))  #赌注结算

total_money.setText('NOW! you have gg')  #宣告破产
