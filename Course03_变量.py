'''
main.py                /* 当前文件名 */
Course03_变量    /* 当前工程名 */

Created by SuHan on December, 16 2015.  /* 创建日期 */
Copyright (c) 2015年 www.china-node.com. All rights reserved.  /* 版权说明 */
'''

'''
1.变量
    在程序语言中,我们可以将变量理解为可以存储数据的一个容器,例如:水杯就是一个可以存储水这种数据的变量,饭桶就是一个可以存储米饭的变量,饭碗
也是可以存储米饭的变量,因此我们发现,不同的变量可以存储数据的类型也各不相同,即使是可以存储相同数据的变量,由于容量不同,它们也分为不同的类型
(如上文提到的饭桶与饭碗),所以在古老的C语言中,我们在创建这个容器的时候不但要指定这个容器的类型,还要指定这个容器的大小.
    但是在python中,我们大可不必这么麻烦,因为python是一个被称之为动态语言的程序语言,它的动态性之一体现在,它的变量是可变的,就是它的容器可
以存放任何类型大小数据,这是因为python语言的编译器是有C语言编写的,所以我们所省略额部分全都由我们的编译器来完成了.所以我们可以不去考虑那些琐碎
的问题,而把精力尽量都用在我们的程序逻辑上,这也是python的一个主要特性,就是简单方便,注重逻辑.
'''
if False:
    #创建一个变量
    #分别用一个数值型与一个字符串型数据赋值给变量,查看变量的类型变化
    var_1 = 1
    print(var_1)
    print(type(var_1))
    var_1 = 'a'
    print(var_1)
    print(type(var_1))

    #根据我们学习过的多种数据类型,创建多个不同类型的变量,输出并检验所有的变量的类型
    var_int = 100
    var_str = "hello world"
    var_bool = True
    var_list = [1,2,3]
    var_tuple = (1,2,3)
    var_set = {1,2,3}
    var_dict = {1:'a',2:'b',3:'c'}
    print(var_int,var_str,var_bool,var_list,var_tuple,var_set,var_dict)
    print(type(var_int),type(var_str),type(var_bool),type(var_list),type(var_tuple),type(var_set),type(var_dict))
else:
    pass

    '''
    1.1变量与内存
        在我们执行 "a = 1" 的时候,我们其实做了两件事,1:在内存中创建了一个可以存储1的数据块,将一个整数1写入其中;2:在内存中生成了一个
    描述该数据存储位置的地址数据,然后将地址写入另一个数据块;那我们的变量就是刚才描述的第二个数据块,它存放了真实数据的地址信息,因此我们可以
    通过变量来访问我们写入的内存数据,在C语言中,我们称这种存放地址的数据块为数据指针.
        但是当我们执行如下代码的时候,想一下内存中数据的变化:
        var_int = 1
        var_int = 2
    这就涉及到程序语言的内存回收机制了,想一想python是如何进行内存回收的.
    '''
    if True:
        #编写一个程序,使两个变量所指向的数据调换
        #创建变量
        var_2 = 1
        var_3 = 2
        var_tmp = None
        #执行指针的调换
        var_tmp = var_2
        var_2 = var_3
        var_3 = var_tmp
        print(var_2,var_3)
    else:
        pass