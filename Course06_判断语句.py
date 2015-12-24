'''
main.py                     /* 当前文件名 */
Course06_判断语句            /* 当前工程名 */

Created by SuHan on December, 17 2015.                         /* 创建日期 */
Copyright (c) 2015年 www.china-node.com. All rights reserved.  /* 版权说明 */
'''

'''
1.if判断语句
在python中判断语句的格式如下:

if <条件表达式>:
    statements
elif <条件表达式>:
    statements
    ...
    ...
else:
    statement
    
如果条件表达式的值为True,则执行对应的statement,如果为False,则执行下一个if分支,值得注意的是,只要执行了某一个if分支,那么程序就会跳出这个
if判断模块,这中执行过程我们称之为首次匹配跳出原则
'''
if False:
    #练习一
    #输入一个数值,判断如果这个数值>0,输出正数,如果<0,则输出负数,如果=0,则输出0
    var_int_1 = int(input("请输入一个任意大小的数:"))
    if var_int_1 > 0:
        print("正数\n")
    elif var_int_1 < 0:
        print("负数\n")
    else:
        print("0\n")
else:
    pass

if True:
    #练习二
    #输入你的身高体重,根据BMI公式(体重除以身高的平方)计算你的健康指数.
    #判断:
    #BMI<18.5       输出过轻;
    #18.5<=BMI<25   输出正常;
    #25<=BMI<28;    输出过重;
    #28<=BMI<=32     输出肥胖;
    #32<BMI        输出严重肥胖;
    var_float_heigh = float(input("输入你的身高(m):"))
    var_float_weight = float(input("输入你的体重(kg):"))
    #这里引入了一个新的内建函数pow(x,y),返回x的y次幂
    var_float_BMI = var_float_weight/pow(var_float_heigh,2)
    print("BMI:%f1.9" %var_float_BMI)
    if var_float_BMI < 18.5:
        print("过轻")
    elif var_float_BMI >= 18.5 and var_float_BMI < 25:
        print("正常")
    elif var_float_BMI >= 25 and var_float_BMI < 28:
        print("过重")
    elif var_float_BMI >= 28 and var_float_BMI <= 32:
        print("肥胖")
    elif var_float_BMI > 32:
        print("严重肥胖")
else:
    pass