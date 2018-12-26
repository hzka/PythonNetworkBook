# -*- coding: UTF-8 -*-
# import sys
# print "你好，世界"
#
# if True:
#     print "Answer"
#     print "True"
# else:
#     print "Answer"
#     print "False"
#
# word = 'kevinhe';sys.stdout.write(word)
# x="a"
# y="b"
# print '---------'
# # 不换行输出
# print x,
# print y,
#
# # 不换行输出
# print x,y
# raw_input("")
# 输出乘积

print 2 * 3
# 输出Hello World
print ("hello world")
# 简单的加法,x和y在这里表示为变量
x = 10
print (x)
print (x + 5)
y = x + 7;
print (y)
# print (z)
# 1.输出0-9的数组。
print list(range(10))
# 2.循环代码结构输出循环列表
# 其中for n in 创建了一个循环，将当前的值赋予变量n来保持计数，将0赋值给n，1、2、3逐次赋值。
# pass命令表示循环结束，下一行返回正常缩进
for n in range(10):
    print (n)
    pass
print ("done")
# 3.打印出数字的平方。
for n in range(10):
    print ("The square of", n, "is", n * n)
    pass
print ("done")


# 1.得到两个数的平均数，输入是两个参数
# def avg(x, y)表示为可重用函数，Python不会让明确这是什么类型的变量，函数定义需要缩进。
# 最后告诉机器返回了什么值。最后使用avg(3,4)进行调用。/ 2.0保证了坚持使用小数部分的数字
# /2的话表示不保留小数部分
def avg(x, y):
    print ("first input is", x)
    print ("second input is", y)
    a = (x + y) / 2.0
    print ("average is", a)
    return a


avg(3, 4)
avg(300, 400)
# 1.新建3*2的数组，其内容被零填充，并将其打印出来,需要导入numpy的包。
import numpy

a = numpy.zeros([3, 2])
print (a)
# 2.更新某些行某些列上面的值，打印出最终结果
a[0, 0] = 1
a[0, 1] = 2
a[1, 0] = 9
a[1, 1] = 12
print (a)
# 3.打印该二维数组中的某个元素
print (a[0, 1])
v = a[1, 1]
print (v)


# 4.若是数组访问越界会报什么样的错，可以看看
# a[0,2]

# 1.可视化数组，对数组中的单元格的值转换成某种色彩。
# 可以简单选择颜色标度，将数值转为某种颜色，也可以将超过某一阈值的单元格涂成黑色，其他的涂为白色
# import matplotlib.pyplot
#
# %matplotlib inline
# 1.定义一个狗的对象和狗的吠叫动作,我们将狗的动作定义为一个函数。作者认为self能够确保函数赋予给正确的对象
# class Dog:
#     def bark(self):
#         print ("woof!")
#         pass
#
#     pass


# 2.创建Sizzles的对象是为一条狗，创建了Dog类的一个实例后调用bark方法，实现狂吠功能。
# sizzles = Dog()
# mutley = Dog()
# sizzles.bark()
# mutley.bark()
# 3.如何将数据变量添加到类中，并添加一些方法来观察和改变数据
# 增加了三个新的函数，第一次创建对象时，会自动调用__init__构造函数，status用于打印狗的姓名和温度
# 最后是setTemp设置狗的温度，第一次创建之后，可以多次设置狗的体温
class Dog:
    def __init__(self, petname, temp):
        self.name = petname
        self.temp = temp

    def status(self):
        print ("dog name is:", self.name)
        print ("dog temperature is:", self.temp)
        pass

    def setTemp(self,temp):
        self.temp = temp
        pass

    def bark(self):
        print ("woof!")
        pass
    pass
lassie = Dog("lassie",37)
lassie.status()

lassie.setTemp(40)
lassie.status()