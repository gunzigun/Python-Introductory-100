# -*- coding: UTF-8 -*-

"""
题目：编写input()和output()函数输入，输出5个学生的数据记录。

程序分析：无。

"""

N_INPUT_STUDENT_NUM = 5

class Student:
    strSchoolNum = ""
    strName = ""
    arrSorce = []

    def __init__(self,strSchoolNum,strName,arrSorce):
        self.strSchoolNum = strSchoolNum
        self.strName = strName
        self.arrSorce = arrSorce
    
Student_array = []

def InputSudent():
    for i in range(N_INPUT_STUDENT_NUM):
        print "please input %dth student info" % (i+1)
        strSchoolNum = raw_input("please input strSchoolNum:")
        strName = raw_input("please input strName:")
        arrSorce = []
        #nLanguage = int(raw_input("please input Language sorce:"))
        #nMath = int(raw_input("please input Math sorce:"))
        #nEnglish = int(raw_input("please input English sorce:"))
        arrSorce.append(int(raw_input("please input Language sorce:")))
        arrSorce.append(int(raw_input("please input Math sorce:")))
        arrSorce.append(int(raw_input("please input English sorce:")))
        Student_object = Student(strSchoolNum,strName,arrSorce)
        Student_array.append(Student_object)

def OutputStudent():
    for i in range(N_INPUT_STUDENT_NUM):
        print "output %dth student info" % (i+1)
        Student_object = Student_array[i]
        strSchoolNum = Student_object.strSchoolNum
        strName = Student_object.strName
        arrSorce = Student_object.arrSorce
        print "strSchoolNum:",strSchoolNum
        print "strName:",strName
        print "Language Sorce:",arrSorce[0]
        print "Math Sorce:",arrSorce[1]
        print "English Sorce:",arrSorce[2]

if __name__ == "__main__":
    InputSudent()
    print Student_array
    OutputStudent()

        

        


        


