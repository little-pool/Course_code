'''
main.py                /* 当前文件名 */
Course01_python简介     /* 当前工程名 */

Created by SuHan on December, 10 2015.  /* 创建日期 */
Copyright (c) 2015年 www.china-node.com. All rights reserved.  /* 版权说明 */
'''

'''
Python语言历史:
Python的作者，Guido von Rossum，确实是荷兰人。
1982年，Guido从阿姆斯特丹大学(University of Amsterdam)获得了数学和计算机硕士学位。
然而，尽管他算得上是一位数学家，但他更加享受计算机带来的乐趣。
用他的话说，尽管拥有数学和计算机双料资质，他总趋向于做计算机相关的工作，并热衷于做任何和编程相关的活儿。

    guido在使用C语言的过程中,发现他虽然可以利用C完成各种工作,但是C语言的编写需要大量的时间,所以他的另一个选择即是shell(shell是当时unix的一个
操作接口),虽然shell可以很简洁的完成工作,但是shell的本质毕竟是调用命令,并不像计算机语言一样拥有数据类型,运算机制等特性,所以利用shell并
不能全面灵活调用计算机的性能.
    guido希望有一种语言,既能够像shell轻松编程,又能够像C语言一样全面调用计算机的所有接口,于是在1989年的圣诞节期间,guido为了打发无聊的假期
在家里开始了python解释器的编译,致力于打造一个介于C语言与shell之间的,易学易用,功能全面,拓展性高的语言.python的易用性体现在,它将很多底层的
处理都交给了编译器来完成,从而凸显在逻辑层面上的程序思考.
    python在刚诞生的时候就特别在意它的可扩展性,不论在底层还是高层,程序员都可以对它进行扩展(在底层可以利用C语言编译为.co文件引入到python中,
在上层,可以编写.py文件作为python的扩展模块)
    在20世纪90年代初,internet的袭来使得程序的开发走向一种新的模式:开源(open source),因此guido为python维护了一个社区,全世界的人都可以将
自己对python的改进提交到guido手中,guido酌情向python的标准库中添加,这就使得python越发壮大.自打python2.0以后,python的开发模式也从milelist
完全转变成开源模式.在今天,python已经开始成熟起来,它的框架已经确立:
    Python语言以对象为核心组织代码(Everything is object)
    支持多种编程范式(multi-paradigm)
    采用动态类型(dynamic typing)
    自动进行内存回收(garbage collection)
    Python支持解释运行(interpret)
    Python有强大的标准库 (battery included)

    在目前来看python虽然在众多语言当中占有这重要的地位(2015年10越语言排行榜top5),但是python仍然有很多需要改进的地方,比如python目前的执行效率
要低于C++以及JAVA,但是它还是一个20出头的小伙子,发展潜力巨大
'''

#第一个python程序:猜字游戏
import easygui      #导入一个GUI第三方模块easygui.py
import random       #导入一个随机功能模块random.py
secret = random.randint(1,99)       #生成一个十进制数字对象用于答案的生成
guess = 0       #代表用户输入的数值
tries = 0       #代表用户输入的次数
icon = 1        #icon标示了游戏是否可以继续,0代表不可以,1代表可以
while icon:     #游戏的循环函数
    choice_beg = easygui.buttonbox("这是一个猜字游戏,数字范围为1~99,你有6次机会","猜字游戏v1.0",choices=("进入游戏","退出"))
    if choice_beg == "进入游戏":
        while guess != secret and tries < 6:
            guess = easygui.integerbox("请输入数字!")
            if guess < secret:
                easygui.msgbox(str(guess) + "你的数太小了!")
            elif guess > secret:
                easygui.msgbox(str(guess) + "你的数太大了!")
            tries += 1
        if guess == secret:
            choice_end = easygui.buttonbox("正确!",choices=("继续游戏","退出游戏"))
            if choice_end == "继续游戏":
                icon = 1
                tries = 0
            else:
                icon = 0
        else:
            choice_end = easygui.buttonbox("你没有机会了!",choices=("继续游戏","退出游戏"))
            if choice_end == "继续游戏":
                icon = 1
                tries = 0
            else:
                icon = 0
    else:
        icon = 0
        pass
print("退出游戏")





