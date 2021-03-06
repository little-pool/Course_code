'''
main.py                    /* 当前文件名 */
Course09_函数式编程               /* 当前工程名 */

Created by SuHan on December, 23 2015.                         /* 创建日期 */
Copyright (c) 2015年 www.china-node.com. All rights reserved.  /* 版权说明 */
'''

'''
1.函数式编程基本概念
函数式编程是一种具有抽象意义的编程模式,我们刚刚讲过函数的定义,如果我们将函数理解为程序中的一个功能模块的话,那么函数式编程就是让程序的最小
单位变成函数,而不是变量,同时,函数的返回值也可以是一个函数,那么整个程序就完全是由函数组成的了,这种编写规范可以让整个程序更安全,这时因为
没有变量的影响,所有的函数输入是固定的,那么输出也一定是固定的,这样的编程模式我们称之为函数式编程
'''
if False:
    #将函数赋值给一个变量
    #通过输出我们可以得出,将函数abs赋值给一个变量var_abs之后,这个变量即拥有了函数的功能,因此函数名也可以理解为一个变量
    def fun01():
        print('hello')
    a = fun01

else:
    pass

    '''
    1.1函数作为参数
    既然函数也可以赋值给一个变量的话,那么我们同样也可以把函数作为变量,传给一个函数,这种传参的方式叫做,以函数作为参数传递
    '''
    if False:
        #需求1:利用一个高阶函数求解两个数值的绝对值之和
        pass

    else:
        pass

    '''
    1.2函数作为返回值
    函数不仅可以作为变量传递给另一个函数,而且他还可以作为一个返回值,作为函数本身的输出
    那么,我们函数执行完毕后,仍然输出一个函数的意义是什么呢?,之前我们把函数定义为,输入数据,经过处理
    输出数据.那么如果输出的还是函数,我们就得不到想要的数据了.
        这就是函数式编程的一个重要体现了,这种函数作为输出的模式我们可以理解为函数的嵌套,即:一个函数中又定义了一个函数,而这个内部函数中
    输出的结果为最终数据,因此我们只要将这个内部函数输出,然后再程序外部再执行这个函数的时候,就得到了我们想要的数据了
    '''
    if False:
        #需求1:定义一个数列求和函数,返回一个可以得到该值的函数
        def fun_sum(*list):

            def fun_in_sum():
                sum = 0
                for i in list:
                    sum += i
                return sum

            return fun_in_sum

        a = fun_sum(1,2,3)

        #直接输出a得到的结果是那个内部的求和函数
        print(a)
        #只有执行这个内部求和函数返回的结果才是数列的和
        print(a())
    else:
        pass

        '''
        1.2.1闭包的概念
        闭包是在程序中经常会遇到的一个概念,我们既然学习完了如何将函数作为返回值,就必须要来了解一下它的概念
        闭包的概念:
            如果在一个内部函数里,对在外部作用域的变量进行引用,而这个外部变量对于外层函数来说,是一个本地变量,那么这个内部函数就被认为是闭包.
        所以说根据上面的例子,我们可以理解,闭包指的就是内部函数fun_in_sum(),因为在它当中,引用了为外部函数的变量list.
            闭包还有一个专业的解释,就是根据不同的配置信息,得到不同的结果,我们可以通过如下例子来体会它的定义.
        '''
        if False:
            def fun_class(x):

                def fun_object():
                    return x+100

                return fun_object

            fun01 = fun_class(10)
            fun02 = fun_class(20)

            print(fun01())
            print(fun02())
        #====================================================================
            def hello(name):
                count = 0

                def counter():
                    nonlocal count
                    count += 1
                    print('hello %s,it is your No.%d access!'%(name,count))
                return counter

            user01 = hello('SuHan')
            user01()
            user01()
            user01()
        else:
            pass

        '''
        1.2.2装饰器的概念
        装饰器的通俗概念就是将一个函数变成一个变量,然后将这个变量放在另一个装饰函数之中,最终执行这个装饰函数,从而实现,在不修改函数的
        情况下,对函数的功能进行任意扩展,这种特性是基于上述讲过的闭包的.
        '''
        if False:
            #在不修改函数本身的情况下定义一个装饰函数，使fun01的输出用""起来
            def fun02(fun):
                def wrapper():
                    return '\"'+fun()+'\"'
                return wrapper

            #定义一个功能函数fun01,功能为以str格式输出传入的参数name
            @fun02
            def fun01():
                return 'hello'

            print(fun01())
        else:
            pass

    '''
    1.3高阶函数
    '''
    if False:
        #详见map&reduce.py
        pass
    else:
        pass

    '''
    1.4匿名函数
        匿名函数简化了函数的创建过程,针对一些简单的函数,我们可以不必按照def的定义方式来定义,这种简单定义的函数不必拥有函数明,因此称之为
    匿名函数,匿名函数的思想仅仅是为了简化程序的语句,但代价是增加了代码的抽象程度,使其具有更紧密的逻辑性.
    '''
    if False:
        a = lambda x : pow(x,2)
        print(a(3))
    else:
        pass
    '''
    1.5偏函数
        偏函数的总用即是将函数的某一个默认参数的值手工固定值,然后返回一个新的函数.从而省去了每次执行时的单独赋值
        例如:
            print()这个函数有一个默认参数为sep='',如果我们想要执行大量的print,但是每次都想让输出间的间隔符赋值为'.'那么我们
        每次都需要为sep赋值为'.'
            有了偏函数之后,我们可以通过functools模块中的partial()方法来为print()创建一个新的函数,来满足我们的特殊需求
    '''
    if True:
        #偏函数案例
        import functools
        print_new = functools.partial(print,sep='.')
        print_new('a','b')
        #偏函数partial()的自定义实现
    else:
        pass




