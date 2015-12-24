'''
main.py                     /* 当前文件名 */
Course07_循环语句            /* 当前工程名 */

Created by SuHan on December, 17 2015.                         /* 创建日期 */
Copyright (c) 2015年 www.china-node.com. All rights reserved.  /* 版权说明 */
'''

'''
1.循环语句概念
    在程序中,计算机的最大优势就是做重复的事情效率极高,所以我们要善于利用这一点,在我们的程序中定义循环语句,来让计算机
高效的工作,例如我们想要计算100!.如果我们执行单步运算的话,我们只能编写100条乘法语句来实现,单如果我们利用循环,可能只需要
几条语句就搞定了,这就是循环语句的优势,书写简单,极大的发挥计算机的运算特性,但我们要提前注意的是,如果我们想要做一个优秀的
程序设计者,我们也是要为计算机考虑的,因为循环计算的高效毕竟会消耗计算机大量的运算资源,因此对循环计算的优化也是我们进阶的
一个重要指标,这里我们可以思考一个最基本的问题,如果我们要对一连串的数值型数据组成的list进行从大到小排序,那我们应该如何设计
排序计算过程,如何优化你的计算过程.
    在python中我们可以执行两种循环,while循环,for迭代,其中while与C语言红的while是一致的,语句格式如下:

while循环语句格式:
==========================
while <表达式1>:
    statement
(在while中仅当表达式1为真的时候,才会执行statement)
==========================

for...in...迭代语句格式:
==========================
for var in interable_object
    statemnet
(其中,var代表一个变量,interable_object为可迭代对象,意思就是使var这个变量依次对该对象的每一个元素进行迭代,再此过程中
每次迭代都会执行一次statement,当迭代结束后,跳出循环)
==========================


因此,while也叫做非定量循环,for也叫做定量迭代,要理解二者的区别
'''
if False:
    pass
else:
    pass

    '''
    1.1while循环语句
    '''
    if False:
        #练习1
        #在一行中,连续输出数字0~10
        var_while_1 = 0
        while var_while_1 < 11:
            print(var_while_1,end = ' ')
            var_while_1 += 1
        print("\n")

        #练习2
        #创建一个包含1~100这100项数据的列表
        var_while_2 = 1
        var_list_1 = []
        while var_while_2 < 101:
            var_list_1.append(var_while_2)
            var_while_2 += 1
        print(var_list_1)
        print(len(var_list_1))

        #练习3
        #求1~100这100个数的总和
        var_while_3 = 1
        var_sum_1 = 0
        while var_while_3 < 101:
            var_sum_1 += var_while_3
            var_while_3 += 1
        print(var_sum_1)

    else:
        pass

    '''
    1.2for...in...迭代
    '''
    if False:
        #由于for语句是指对可迭代对象进行迭代处理,所以你要明白什么叫做可迭代类型的对象,我们可以判断任意一个数据类型是否具有可迭代属性
        #利用isinstance(object,itarable)来判断一个对象是否可迭代
        from collections import Iterable
        var_int_1 = 1
        var_float_1 = 1.11
        var_str_1 = "abc"
        var_list_2 = [1,2,3]
        var_tuple_1 = (1,2,3)
        var_dict_1 = {1:'a',2:'b'}
        print(isinstance(var_int_1,Iterable))
        print(isinstance(var_float_1,Iterable))
        print(isinstance(var_str_1,Iterable))
        print(isinstance(var_list_2,Iterable))
        print(isinstance(var_tuple_1,Iterable))
        print(isinstance(var_dict_1,Iterable))

        #练习1
        #迭代输出list中每一个元素
        var_list_3 = [1,'b',['c']]
        for var_for_1 in var_list_3:
            print(var_for_1,end=' ')
        print("\n")

        #迭代输出字典中的每一个value
        var_dict_2 = {1:'a',2:'b'}
        for var_for_2 in var_dict_2:
            print(var_dict_2.get(var_for_2),end=' ')
    else:
        pass
    '''
    1.3break与continue的作用
    在循环的执行过程中,如果我们不想让整个循环都执行完,想在某一时刻退出循环,或者跳过单次循环的话,我们就需要在循环过程中
    利用好这两个功能
    '''
    if True:
        #遍历整个列表,一旦发现字符串"break",即刻退出循环
        var_list = [1,2,3,"break",4,5]
        for var_tem in var_list:
            print(var_tem,end=' ')
            if var_tem == "break":
                break

        print('\n')

        #遍历整个列表,一旦发现字符串"break",跳过本次循环,然后继续执行
        for var_tem in var_list:
            print(var_tem,end=' ')
            if var_tem == "break":
                continue
    else:
        pass


'''
2.简单的排序算法
排序算法可以检验大家对判断以及循环语句的理解以及熟练程度,大家思考一下,如果我想对一个乱序的数值list进行从大到小排序,我们都可以怎样处理
这里的对同一个目的的不同处理方法,我们在程序语言中统称为算法,算法是门艺术,能够反应你处理问题的思维,以及将这种思维转化为计算机语言的能力.
目前我们可以轻易理解的排序算法有如下几种:
1.选择排序法
2.冒泡排序法
3.希尔排序
4.归并排序
5.快速排序
6.堆排序
'''
if False:
    pass
else:
    pass

    '''
    2.1选择排序
    算法逻辑:
        先遍历list中所有的元素,将最小的元素与第一个元素交换位置,然后遍历省下的素有元素,再将最小的与第二个交换位置,以此类推
    '''
    if False:
        #选择排序练习
        #生成包含10个0~100间随机数的list
        import random
        var_list= []
        for var_tem in range(10):
            var_list.append(random.randint(0,100))
        print(var_list)

        #排序部分
        for i in range(0,len(var_list)):
            #var_max用于存储最小数值在list中的位置
            var_min = i
            #在后面的元素中选择最大的元素,将其位置赋值给var_max
            for j in range(i+1,len(var_list)):
                if var_list[j] < var_list[var_min]:
                    var_max = j
            #将选出的var_min位置的元素与外循环开头元素相交换
            var_list[i],var_list[var_max] = var_list[var_max],var_list[i]
        print(var_list)
    else:
        pass


    '''
    2.2冒泡排序
    算法逻辑:
        先比较list中的前两个元素,如果第一个大于第二个,那么执行"冒泡",即交换两个元素位置;然后再判断,如果第二个元素大于第三个元素,则
    继续执行冒泡,以此类推,经过第一轮冒泡后,可以保证list中最后一个元素为最大的元素,然后在用同样的方法处理list中的第0到第len(list)-1项
    '''
    if False:
        #选择排序练习
        #生成包含10个0~100间随机数的list
        import random
        var_list= []
        for var_tem in range(10):
            var_list.append(random.randint(0,100))
        print(var_list)

        #排序部分
        for i in range(0,len(var_list)):
            for j in range(0,len(var_list)-1-i):        #这里如果没有-1的话,就会导致内存溢出
                if var_list[j] > var_list[j+1]:
                    var_list[j],var_list[j+1] = var_list[j+1],var_list[j]
        print(var_list)
    else:
        pass


