# Function:accept a quiz score as an input and prints out the corresponding grade
#Author:worthurlove
#Date:2018.10.8
score_grade = {5: 'A', 4: 'B', 3: 'C', 2: 'D', 1: 'E', 0: 'F'}
'''
定义数据字典，将测试分数与成绩一一对应
'''


def get_grade(score_grade):
    score = int(input('请输入0到5之间的测试分数:'))
    if (score < 0 | score > 5):
        print("请输入合法分数")
        '''
        对输入进行合法性判断 
        '''
    else:
        print('成绩为：' + score_grade[score])
        '''
        输出对应成绩
        '''


get_grade(score_grade)