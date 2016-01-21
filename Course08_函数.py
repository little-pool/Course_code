'''
main.py                     /* 当前文件名 */
Course07_函数               /* 当前工程名 */

Created by SuHan on December, 20 2015.                         /* 创建日期 */
Copyright (c) 2015年 www.china-node.com. All rights reserved.  /* 版权说明 */
'''

'''
1.函数的基本概念
函数是程序的第一个级别的抽象,就好比咱们的社会从农业时代走向了工业时代,而函数本身就像是工业时代的工厂车间一样产生为社会不停的生产产品
在程序设计中使用函数有如下几个好处,1:实现代码复用,提高开发效率;2:进一步对程序进行抽象,使程序更具有逻辑性;
例如:
    我们想要求解一个长方形l1的面积,l1.wide=10,l1.length=20,那么求这个面积的程序为:
    area1 = l1.wide*l1.length
    当我们想要求解另一个长方形的面积时,还需要令一行代码:
    area2 = l2.wide*l2.length

如果我们用函数的思维来处理这个问题的话,我们首先创建一个能够计算矩形面积的函数

<矩形计算器>(矩形长,矩形宽)
    面积 = 长*宽
    返回 面积

其中,"举行计算器"叫做函数名;"矩形长,矩形宽"叫做函数的参数,"面积"叫做函数的返回值,一个基本的函数也是由这几个元素组成的,总结下来就是,向函数
输入相应的参数,获取函数通过参数计算出来的返回值,这就是函数的执行原理
'''

if False:
    #1.函数的创建,与调用
    #需求1:输入连续数字的范围,求连数字的和
    def sum_int(start,end):
        sum = 0
        for i in range(start,end+1):
            sum += i
        return sum
    print(sum_int(1,10))


    #需求2:输入纯数字组成的list,对数字进行排序,返回从小到大排好序的list
    def sort_list(list):
        #对传入的list进行排序,方法为选择排序
        for i in range(0,len(list)):
            min = i
            for j in range(i+1,len(list)):
                if list[j] < list[min]:
                    min = j
            list[i],list[min] = list[min],list[i]
        return list
    print(sort_list([2,1,3,5,4,7,6,9,8]))
else:
    pass

'''
2.函数的参数类型
函数参数的类型一共有如下几种:
    1.位置参数
    2.默认参数
    3.可变参数
    4.关键字参数
    5.命名关键字参数
'''
if False:
    pass
else:
    pass

    '''
    2.1位置参数
    我们首先需要知道两个概念,型参与实参
    例如这个函数:
    sum_int(start,end),其中,start与end就是函数的形式参数,因此形参就是在定义函数时声明的待传入数据
    sum_int(1,10),在调用函数时,输入的1,10就是实际参数,因此实参就是在执行函数时真正传入到函数中的数据
    那么位置参数就是指这样形参与实参一一对应的参数
    '''

    '''
    2.2默认参数
    如果我们有这样一个需求,传入一个整形数值,默认返回这个数值的2次幂,但如果在参数中指定了第二个参数为3,那么返回实参的3次幂
    '''
    if False:
        #定义一个求参数x的n次幂的函数,要求默认返回x的2次幂
        def power(x,n = 2):
            resault = x
            for i in range(0,n-1):
                resault *= x
            return resault
        print(power(2,32))
    else:
        pass

    '''
    2.3可变参数
    上面两种参数的设计都是在参数已知的情况下,来定义并执行的函数,但是如果我们并不知道将要传入该函数的参数的个数怎么办呢?
    如果有这种情况,我们可以这样做,去准备一个盒子,专门存放不确定会不会传进来的参数,然后用到哪个参数,我们再去这个盒子里面把它找出来
    '''
    if False:
        #将前两个参数定义为位置参数,除了位置参数之外所有的实参都传递到*c这个盒子里,然后将盒子里的数据逐一输出
        def test_fun01(a,b,*c):
            print(a)
            print(b)
            print(len(c))
            for i in c:
                print(i)
            return c

        #由于函数的返回值为盒子c,所以我们将c提取出来
        c = test_fun01(100,200,"abcd",[1,2,3],'SuHan')
        #根据返回结果我们可以发现,这个盒子就是我们学过的元组(tuple)
        print(type(c))
        print(c)
    else:
        pass

    '''
    2.4关键字参数
    在可变参数中,函数会利用一个list存放我们添加的,除位置参数之外的所有参数,但要注意的是这些参数仅仅是实参,是没有形参相对应的.
    介于上述情况,我们是否可以在可变参数的基础上,为我们传入的所有实参对应一个形参呢?
    '''
    if False:
        #这里函数会将除位置参数之外的所有的形参与实参组合成一个字典,放入到c这个盒子里
        def test_fun02(a,b,**c):
            print(a)
            print(b)
            print(len(c))
            for i in c:
                print(i + ':' + str(c[i]))
            return c
        c = test_fun02(100,200,name='SuHan',age=23)
        #可以看出,函数拿了一个字典来存储所有的关键字参数
        print(type(c))
        print(c)
    else:
        pass

    '''
    2.5命名关键字参数
    上述的关键字参数有一个缺陷,就是一旦有了这个字典,我们就可以肆无忌惮的向函数中添加自定义的参数了,这样不是很好控制嘛.
    因此我们引入命名关键字参数,就是指,我们规定用户可以添加的参数的形参名,以至于用户只可以传入指定的一个或几个关键字参数
    '''
    #这里我们要记住,位置参数与命名关键字参数中间是由'*'分隔开的,传入位参时不用指定形参名,而传入命名关键字参数时是必须指定形参名的
    if False:
        def test_fun03(a,b,*,name,age):
            print(a)
            print(b)
            print(name)
            print(age)
            return None
        #这时我们发现在传入命名关键字参数时,不指定形参名会报错
        #test_fun03(100,200,'SuHan',23)
        test_fun03(100,200,name='SuHan',age=23)
    else:
        pass


    '''
    2.6混合参数
    我们提到的5中参数中除了可变参数与命名关键字参数无法一起使用之外,其余参数都是可以混合使用的.
    '''
    if False:
        def test_fun04(a,b,*c,**d):
            print('a=',a,'b=',b,'c=',c,'d=',d)
            return c
        test_fun04(1,2,3,4,5,6,d1=7,d2=8)
    else:
        pass

'''
3.函数的互相调用
既然一个函数我们就可以理解为一个模块或一个功能,那么我们就可以利用多个函数来组装成新的函数了,这就叫做函数间的互相调用
例如:
    将一个列表中每个元素的绝对值按从小到大排列,这样一个需求我们就可以将它由两个函数组装而成.
    函数1:将列表中所有元素取绝对值
    函数2:将列表元素从小到大排序
'''
if False:
    #函数1:将列表中的所有元素取绝对值
    def absolute(list_var):
        list_new = []
        for i in list_var:
            list_new.append(abs(i))
        return list_new
    print(absolute([-1,2,-3]))

    #函数2:排序函数,算法为冒泡
    def sort(list_var):
        for i in range(1,len(list_var)):
            for j in range(0,len(list_var)-i):
                if list_var[j] > list_var[j+1]:
                    list_var[j] , list_var[j+1] = list_var[j+1] , list_var[j]
        return list_var
    print(sort([2,4,5,3,1]))

    #函数3:组合函数
    #将两个函数拼接在一起,形成新的函数,完成将list中元素取绝对值排序功能
    def absolute_sort(list_var):
        #在拼装过程中要注意两个组件函数的返回值问题
        list_new = absolute(list_var)
        return sort(list_new)

    print(absolute_sort([-9,5,-3,1,10,8,7]))
else:
    pass

'''
4.递归函数
函数既然可以互相调用,那么我们再函数内部调用函数本身即叫做函数的递归,递归思维就是指利用追溯的方法来解决复杂问题.
例如,斐波那契数列问题,阶乘问题,汉诺塔问题,二叉树的遍历,都会用到递归
'''
if False:
    pass
else:
    pass

    '''
    4.1阶乘问题
    5! = 5*4*3*2*1,用递归可以把这个问题理解为:5!=5*4!;4!=4*3!...
    那么我们只要将问题追溯到1!=1就可以反推任何数字的阶乘了,在计算机中,是用栈的方式来处理的,着咱们不需要理解
    '''
    if False:
        def recursion_fatorial(n):
            if n == 1:
                return 1
            else:
                return n*recursion_fatorial(n-1)
        print(recursion_fatorial(3))
    else:
        pass

    '''
    4.2趣味问题:
    有5个人并排而坐,我们想知道第一个人的年龄,第一个人说他比第二个人大两岁,第二个人说他比第三个人大两岁,第三个人说他比第四个人大两岁
    第四个人说他比第五个人大两岁,第五个人说他10岁;
    '''
    if True:
        def get_age(num):
            if num == 5:
                return 10
            else:
                return get_age(num+1)+2

        print(get_age(5))

    else:
        pass



