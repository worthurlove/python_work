#Function:show how the value change of chaos.py
#Author:worthurlove
#Date:2018.10.8

chao1 = [0] * 11
chao2 = [0] * 11

#定义两个列表用于存储迭代后的数据


def chaos(x, chao):
    chao[0] = x
    for i in range(1, 11):
        chao[i] = 3.9 * chao[i - 1] * (1 - chao[i - 1])
        '''
        混沌公式计算10次迭代后的数值，并用列表记录
        '''
    return chao


x, y = map(float, input('请输入两个介于0和1之间的小数：').split())
'''
一次性输入两个数据进行对比
'''
chaos(x, chao1)
chaos(y, chao2)

print("{0:<5}{1:>10.6}{2:>15.6}".format('index', x, y))  #输出标题栏

for i in range(1, 11):
    print("{0:<5}{1:>10.6}{2:>15.6}".format(i, chao1[i], chao2[i]))  #格式化输出数据
