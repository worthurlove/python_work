#Fuction:read a file which recods the scores of student,calculate and print the name of student who has the best GPA
#Author:worthurlove
#Date:2018.10.19


#定义学生类
class Student:
    #初始化函数，输入学生的姓名，课时和学分
    def __init__(self, name, hours, qpoints):
        self.name = name
        self.hours = float(hours)
        self.qpoints = float(qpoints)

    #获取学生的姓名
    def getName(self):
        return self.name

    #获取学生的课时
    def getHours(self):
        return self.hours

    #获取学生的学分
    def getQpoints(self):
        return self.qpoints

    #计算GPA
    def gpa(self):
        return self.qpoints / self.getHours()


#找出GPA最高的学生
def bestGpa(file_read):
    best_student_name = []#将GPA最高的学生存储到list里
    current_best = 0#当前的最高GPA
    for line in file_read:#逐行读取文件
        name,hours,qpoints = line[:-1].split()#拆分文件内容
        bestStudent = Student(name,hours,qpoints)#建立学生对象

        if bestStudent.gpa() > current_best:#如果当前学生GPA最高，则将列表清空并其加入列表
            current_best = bestStudent.gpa()
            best_student_name = [bestStudent.getName()]

        elif bestStudent.gpa() == current_best:#如果当前学生GPA等于最高GPA，则将其加入列表
            best_student_name.append(bestStudent.getName())

        else:#其余情况则跳过
            continue

    #打印出GPA最高的学生名单
    print('GPA最高的学生是：')
    for name in best_student_name:
        print(name)


if __name__ == '__main__':
    
    file_read = open('records.txt','r')#打开文件

    bestGpa(file_read)#找出GPA最高的学生

    file_read.close()#关闭问件