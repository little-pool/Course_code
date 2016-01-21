'''
map&reduce.py                               /* 当前文件名 */
Course09_函数式编程                          /* 当前工程名 */

Created by SuHan on January, 4 2016.                         /* 创建日期 */
Copyright (c) 2016年 www.china-node.com. All rights reserved.  /* 版权说明 */
'''

'''
MAP功能的实现
map()函数接收两个参数，一个是函数，一个是Iterable，map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回
'''
if False:
    #python中map功能测试
    def power(x,n = 2):
        return pow(x,n)
    l1 = [1,2,3]
    l2 = map(power,l1)
    print(list(l2))


    #map的自定义实现
    def map_new(fun,list):
        list_new = []
        for i in list:
            list_new.append(fun(i))
        return list_new
    l3 = map_new(power,l1)
    print(l3)


    def toupper(c):
        if isinstance(c,str):
            return c.upper()
    l4 = ['a','b','c']
    print(map_new(toupper,l4))
else:
    pass
'''
REDUCE功能的实现
reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算
'''
if True:
    #python中reduce功能的实现
    from functools import reduce
    def reduce_sum(x,y):
        return x+y
    l5 = [1,2,3,4,5,6,7]
    print(reduce(reduce_sum,l5))


    #reduce的自定义实现
    def reduce_new(fun,list):
        tem = list[0]
        for i in range(1,len(list)):
            tem = fun(tem,list[i])
        return tem
    print(reduce_new(reduce_sum,l5))

else:
    pass
