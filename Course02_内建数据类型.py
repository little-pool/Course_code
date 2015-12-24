'''
main.py                /* 当前文件名 */
Course02_内建数据类型     /* 当前工程名 */

Created by SuHan on December, 15 2015.  /* 创建日期 */
Copyright (c) 2015年 www.china-node.com. All rights reserved.  /* 版权说明 */
'''

'''
1.bool类型
这种类型的数据只有两种取值,True或者Fales,这两种取值经常被人们混淆为1或者0,其实我们所谓的
1或者0的数据类型为数值型(之后讲),利用isinstance函数可以做一个简单的解释
'''
if False:
    #数字的0与1并不是bool类型的
    print(isinstance(0,bool))
    print(isinstance(1,bool))
    #python中有两个常量可以表示布尔型的两个值
    print(isinstance(True,bool))
    print(isinstance(False,bool))
    #表达式的结果为布尔型数据
    print(isinstance(1>2,bool))
    print(1>2)

    #一个python中存在的问题,bool类型的数据可以被当成数值类型的数据对待
    #这是极其不可合理的数据处理方式,严禁这样使用bool型的数据
    print(True+True)
    print(True == 1)
else:
    pass

'''
2.数值类型
数值类型数据分为两种,1:整数;2:浮点数,我们并不用在在创建时对这两种数值进行区分,因为python
可以通过数值是否包含小数点自动为数值分类,我们可以利用type函数来判断数据的类型
'''
if False:
    #判断一个整数的数据类型
    print(type(1))
    print(isinstance(1,int))
    #判断一个浮点数的数据类型
    print(type(1.1))
    print(isinstance(1.1,float))
else:
    pass

    '''
    2.1在整数与浮点数之间互相抓换
    有时候我们需要将获取的小数取整,这时就要用到一些函数来强制转换数据的类型,例如int,float
    '''
    if False:
        #将整形数据转换成浮点型数据
        print(float(1))
        #将浮点型数据转换成整形数据,通过输出我们可以发现,这种转换并不是四舍五入,而是取整
        print(int(1.1))
        print(int(1.5))
        #负数的取整方向为"朝向0的方向"
        print(int(-1.5))
    else:
        pass

    '''
    2.2用科学计数法表示过大或者过小的数值型数据
    如果我们想表示非常大的数,我们可以这样写1000000000,或者0.00000001
    这样书写出来的代码非常不易阅读,因此表示复杂数值时,我们选择用科学表示方式
    '''
    if False:
        #表示一个很大的正整数
        print(1.1e10)
        #表示一个很小的浮点数
        print(1.1e-10)
        #复杂数值间运算
        print(1.1e-1*1e2)
    else:
        pass

'''
3.字符串类型
字符串是由任意数量的字符组合而成的数据,例如某人的名字,电话号码等等数据都需要以字符串的方式表示
在python中字符串是以单引号'或双引号"括起来的任意文本，比如'abc'，"xyz"等等。
请注意，''或""本身只是一种表示方式，不是字符串的一部分，因此，字符串'abc'只有a，b，c这3个字符。
如果'本身也是一个字符，那就可以用""括起来，比如"I'm OK"包含的字符是I，'，m，空格，O，K这6个字符。
'''
if False:
    #输出一个字符串
    print('abcde')
    #输出一个带有'字符的字符串
    print("'abcde'")
    #输出一个即包含',又包含"的字符串
    print("\"他说:'我可以输出包含'''和'\"'的字符串'")
    #输出一个包含\的字符串
    print("\"他说:'我可以输出包含'\\'的字符串\"")
else:
    pass

'''
4.列表类型
在python中,列表这种数据类型拥有很高的地位,因为python的列表相比于C语言中的数组不知道强大多少倍
首先列表是用来存放一组数据的集合,在C语言中我们在一个集合中只能存放同一个类型的数据,例如:
[1,2,3],或者['a','b','c']而且我们在创建集合时必须指定这个集合的"容量",这些都直接导致了
在C数组使用的繁琐性.
    那么在我们的python中这个集合就会看起来非常灵活,因为我们可以在同一个集合中放入任意类型的数据
例如:[1,'a',[2,'b']]这个集合中就包含了三种类型的数据,数值类型,字符串类型,列表类型.非常强大吧.
而且python还为我们提供了很多对于列表的操作接口,例如pop,insert,append等等函数,方便了我们对于
列表中数据的操作
'''
if False:
    #创建一个列表,这里引入了变量的概念(如:list_1),我们在下一节学习
    list_1 = [1,2,3,'a','b','c']
    print(list_1)
    #输出列表中的某一项数据,这里要清楚在列表中表项的索引值是从0开始的
    print(list_1[0])
    print(list_1[3])
    #查看列表中不同数据的类型,证明python的列表是可以同时存放多种类型的数据的
    print(type(list_1[0]),type(list_1[3]))
else:
    pass

    '''
    4.1列表的数据操作
    我们在基础部分可以做到如下几种对列表的操作:1.插入;2.追加;3.删除;4.替换
    '''
    if False:
        #创建一个新列表
        list_2 = [1,2,3,4,5]

        '''
        4.1.1插入
        '''
        #在列表的任意位置添加元素:insert()函数
        list_2.insert(0,0)
        print(list_2)

        '''
        4.1.2追加
        列表的追加有两种方式,即追加列表元素与追加可迭代对象(例如另一个列表等...)
        '''
        #在列表末尾追加元素:append()函数
        list_2.append(6)
        print(list_2)
        #在列表末尾追加列表或其他可迭代对象
        list_2.extend(['a','b','c'])

        '''
        4.1.3删除
        对列表元素的删除分为根据索引删除与根据数据删除用到的函数分别是pop与remove
        '''
        #在列表中删除任意元素:pop函数
        list_2.pop(0)#删除列表中第一个元素
        print(list_2)
        list_2.pop(-1)
        print(list_2)
        
        #在列表中根据列表的数据删除元素:remove函数
        list_2.remove('a')#删除列表中值='a'的元素
        print(list_2)

        '''
        4.1.4替换
        '''
        #在列表中替换某一个元素
        list_2[0] = "First Item"
        print(list_2)
    else:
        pass

'''
5.元组
元组(tuple)可以理解为一个不可变的列表,因此tuple一旦被创建,里面的元素就不可更改
在tuple中我们没有类似于append,pop等方法进行操作,因此我们只可以对元组内的数据进行访问
'''
if False:
    #创建一个元组对象,tuple与list的区别在于
    tuple_1 = (1,2,3,'a','b','c')
    print(tuple_1)
    #根据索引访问tuple中的元素,这种索引方式与list一样,-1代表最后一项,0代表第一项
    print(tuple_1[0])
    print(tuple_1[-1])

    #tuple的优势就是一旦创建,无法修改,这使得tuple中的数据变得非常安全,而且tuple的运行
    #速度要快于list,所以如果你的需求仅仅是对很多常量的遍历,那么推荐利用tuple来存储这些数据
else:
    pass
    '''
    5.1元组与列表的互相转换
    在python中有很多非常强大的python内建函数(built-in function)
    其中就有一个tuple()函数,接收一个列表参数,返回一个元组对象
    另一个就是list()函数,接收一个元组对象,返回一个列表对象
    所以可以总结为:tuple()冻结list;list()融化tuple
    '''
    if False:
        #将一个列表转化为一个元组
        list_3 = [1,2,3]            #创建一个新列表
        tuple_2 = tuple(list_3)     #将列表转换成元组
        print(tuple_2)              #输出元组
        print(type(tuple_2))        #判断对象类型

        #将一个元组转化成列表
        list_4 = list(tuple_2)      #将上文生成的元组转换成列表赋值给list_4
        print(list_4)               #输出list_4
        print(type(list_4))         #判断对象类型

        list_4.extend([4,5])        #验证列表的可变性
        print(list_4)
    else:
        pass

'''
6.集合
集合这种类型也是用来存储多个数据的数据类型,只不过它是一个无序的,只会保存唯一值的"容器"
所以我们会经常用这种对象来做索引目录,它与list一样也是同时可以存放多种类型的数据
'''
if False:
    '''
    6.1创建集合
    '''
    #创建一个集合对象,它的创建方法为tem = {}
    set_1 = {1,2,3}
    print(set_1)

    #创建一个空集合,在结果中显示,该"空集合的类型为dict"这很奇怪,这是因为在python中,默认是不
    #可以用{}来表示空集合的,{}是用来创建字典这种类型的标识符
    set_2 = {}
    print(type(set_2))

    #创建一个真正的空集合
    set_3 = set()       #这才是真正创建空集合的语句
    print(set_3)        #输出空集合是会返回set()
    print(type(set_3))  #判断该对象的类型

    '''
    6.2对集合中的数据进行操作
    '''
    #对集合数据的操作,我们需要学习对set的三种操作,1:添加;2:更新;3:删除
    #创建一个新的集合
    set_4 = {1,2,3}

    #在集合中添加元素
    #通过输出表明,所有的元素在集合中是无序存放的,因此集合不会用位置的索引
    #来访问集合内的元素,例如:像list一样的list[0],因为当我们学习dict的时候我们就会发现
    #set中的数据本身就起到了索引的作用,我们称set中的数据为key,在dict中key对应的数据称之为
    #key_value
    set_4.add('5')
    set_4.add('4')
    print(set_4)

    #在集合中添加集合对象
    #我们在之前的set_4的基础上又为set添加了{3,4,5,6},那么最终的set_4会去重后添加
    set_4.update({3,4,5,6})
    print(set_4)

    #在update中不但可以引入集合对象,还可以引入任何其他的可迭代对象例如list或者tuple
    set_4.update([5,6,7])       #在set中添加list
    print(set_4)
    set_4.update((6,7,8))       #在set总添加tuple
    print(set_4)

    #在集合中删除元素
    #这里我们又4个函数可以利用,1:remove;2.discard;3.pop;4.clear
    #1.remove()函数
    #删除集合中的任意项,如果没有匹配不会中断程序,将错误作为函数的返回值
    set_5 = {1,2,3,4}
    set_5.remove(4)
    print(set_5)
    #print(set_5.remove(4))     #该函数返回了一个key_error的异常
    #2.discard()函数
    #删除集合中任意项,如果没有匹配不会中断函数,并没有任何错误返回
    set_6 = {1,2,3,4}
    set_6.discard(4)
    print(set_6)
    print(set_6.discard(4))     #该函数的返回值为空,说明虽然发生了key_error,该函数也不会报错
    #3.pop()函数
    #pop函数不接收任何参数,作用为从set的起始位置删除一个元素,并将该元素最为返回值
    #但是一般来说set是不会用位置进行索引的,所以pop我们用的不多
    set_7 = {1,2,3,4}
    print(set_7)
    set_7.pop()
    print(set_7)
    set_7.pop()
    print(set_7)
    #4.clear()函数
    #该函数会删除set中的所有元素,仅省下一个空集合,然后将原set覆盖
    set_8 = {1,2,3,4}
    set_8.clear()
    print(set_8)        #这里输出了一个set(),代表空集合的意思,而不是{},因为{}代表dict
else:
    pass

    '''
    6.3对set的一些特殊操作
    由于set存储的为无重复无序元素,所以我们对set可能有如下需求:
        1.判断某一个元素是否在set中存在:in
        2.判断两个set的交集都有哪些元素:intersection()
        3.判断两个set的非集都有那些元素:symmetric_difference();difference()
        4.判断两个set的或集都有哪些元素:union()
    '''
    if False:
        #判断某个元素是否存在于某个set中,set所支持的in操作符可以返回一个bool类型的值
        set_9 = {1,2,3,4}
        print(3 in set_9)                           #判断3是否在set_9中存在
        print(5 in set_9)                           #判断5是否在set_9中存在

        #查案两个set的交集,intersection()函数
        set_10 = {2,3,4,5}
        print(set_9.intersection(set_10))           #set_9与set_10的交集为{2,3,4}

        #查看两个set的非集,symmetric_difference函数
        print(set_9.symmetric_difference(set_10))   #set_9与set_10的非集为{1,5}

        #查看在一个set中但是不再另一个set中的元素
        print(set_9.difference(set_10))             #set_9中存在但set_10中不存在
        print(set_10.difference(set_9))             #set_10中存在但set_9中不存在

        #查看两个集合的或集
        print(set_9.union(set_10))                  #输出set_9与set_10的或集
    else:
        pass

'''
7.字典
字典在python中全称叫做dictionary,这是一种特殊的数据容器,在这个容器中,每一个元素都有两个
部分:key以及key_value,因此它相对于list的优势就是索引速度快.举例来说,如果你用list结构来
存储100个学生的成绩,那么你至少需要两张列表来分别存放学生的id与成绩,在提取数据时,我们需要
先索引学生id,再索引成绩,最终才能得到学生与成绩的映射关系.
    如果这个需求用dict来处理的话,我们只需要一个dict对象就可以将学生与成绩的映射存储,并且
只需索引学生id就可以直接通过id提取成绩数据,非常方便.dict在其他程序语言中也叫做map(映射)
'''
if False:
    #创建字典
    #字典中每一个元素都是key与value的组合,它们用:相关联
    dict_1 = {1:'a',2:'b',3:'c'}
    #字典儿输出
    print(dict_1)
    #获取字典内的数据
    #这里要注意,我们只能通过字典中的key来获取对应的value,而不能反向访问
    print(dict_1[1])        #通过key 1访问对应的数据'a'
    #print(dict_1['a'])      #无法通过'a'访问对应的key
else:
    pass

    '''
    7.1字典的操作
    对字典的操作完全是基于key的,不论是检索,删除,还是修改
    '''
    if False:
        '''
        7.1.1插入数据
        '''
        #向字典中添加键值对,如果指定的key在当前字典中已经存在,那么新指定的value会覆盖原有的value
        dict_2 = {1:'a',2:'b',3:'c'}
        dict_2[4] = 'd'
        print(dict_2)
        dict_2[4] = 'dd'
        print(dict_2)
        '''
        7.2检索数据
        '''
        #判断dict中是否存在某个key:in方法
        print(1 in dict_2)      #in操作检索dict中的所有key,返回一个bool值
        print(5 in dict_2)
        #利用key直接提取value,不过这种方法在key不存在的时候会中断程序,没有异常处理机制
        print(dict_2[1])
        #print(dict_2[5])
        #利用get()方法提取dict中的value,这种方法在key不存在的时候会返回None,而不会中断程序
        print(dict_2.get(1))
        print(dict_2.get(5))    #通过这个输出我们发现,利用这种方法提取时,即使指定的key不存在,程序也不会中断,只是返回一个None

        '''
        7.3删除数据
        '''
        #根据key删除数值对
        #如果在pop后只指定一个参数,那么返回值为删除键值对的value
        dict_3 = {1:'a',2:'b',3:'c'}
        print(dict_3.pop(1))
        print(dict_3)

        #如果pop后指定的键值在dict中不存在,那么pop返回一个keyerror异常
        #dict_3.pop(5)
        #dict_3.pop(5,default='there is no key which you specified in the dict')

        #删除dict中所有的键值对
        dict_3.clear()
        print(dict_3)
    else:
        pass

