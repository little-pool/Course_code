'''
main.py                     /* 当前文件名 */
Course05_输入与输出          /* 当前工程名 */

Created by SuHan on December, 16 2015.                         /* 创建日期 */
Copyright (c) 2015年 www.china-node.com. All rights reserved.  /* 版权说明 */
'''

'''
1.输出函数
在python的内建函数中拥有强大的输出函数print()
print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)
我们目前还没有学习过函数的参数,所以我们先来体验一下这个函数的功能,这个print函数支持灵活输出,以及文件的写入,非常强大
'''
if False:
    #创建一个字符串,用于检验输出
    var_str_1 = "hello,world!\nhello,python!\n"
    #直接输出
    print(var_str_1)

    #sep参数是为多次输出的数据之间添加分隔符的意思,体验一下
    print(1,2,3,4,5)
    print(1,2,3,4,5,sep='->')

    #end参数是迭代输出时用到的参数,我们仍然来体验一下
    for i in range(0,11):
        print(i,end=' ')
    print('\n')

    #file这个参数是用于文件写入的参数,它后面可以添加文件对象,体验一下
    import sys
    print(sys.path[0])
    var_file_1 = open('file_test',mode='w')
    print('hello,world!!!',file=var_file_1)
else:
    pass

    '''
    1.1格式化输出
    我们上述讲解的输入方式仅仅是将所指定的变量或者常量原样输出,并没有做任何的加工,比如我只想输出一个保留2位小数的float类型数据
    我们就需要格式化我们的输出数据,这种格式化输出很简单也很常用.
    '''
    if False:
        #格式化输出一个浮点数,要求只保留两位小数
        var_float_1 = 1.111
        print("%.2f" %var_float_1)
        #格式化输出一个整数,要求在整数不足两位数时,前面用0补位
        var_int_1 = 1
        print('%02d' %var_int_1)
        #格式化输出字符串
        var_str_name = 'SuHan'
        var_int_age = '23'
        print("%s is already %s years old"%(var_str_name,var_int_age))
    else:
        pass

'''
2.输入函数
如果我们需要让用户自己为变量输入数据,那我们就需要用到python为我们提供另一个内建函数input,这个函数只有一个参数,格式为:
input([prompt])
其中prompt代表提示的意思,可以在你的输入位置的前面给予输入提示
'''
if True:
    #要求手工输入你的姓名和年龄,然后利用格式化输出将两个信息分行输出
    #这里注意一个问题,我们用input输入的所有数据都默认被认为是str类型的,所以你如果想更改输入数据的类型,需要用之前我们提到的强制类型转换
    var_input_name = input('Input your name:')
    var_input_age = int(input('Input your age:'))
    print("Name:%s\nAge:%s" %(var_input_name,var_input_age))
    print(type(var_input_name),type(var_input_age),sep='\n')
else:
    pass