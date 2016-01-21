'''
main.py                          /* 当前文件名 */
Course10_类与对象               /* 当前工程名 */

Created by SuHan on January, 21 2016.                         /* 创建日期 */
Copyright (c) 2016年 www.china-node.com. All rights reserved.  /* 版权说明 */
'''
'''
1.抽象的概念
    类和对象都是哲学思想中的两个基本概念

    类代表:    集合,抽象,描述
    对象代表:  单个,具体,实在

    类具有两种元素:属性,方法
    对象是构成世界的基本单位

    实例:电脑,CPU,主板,内存,制图,开发,计算
'''

if True:
    class PC():
        #为PC类设置属性,并为属性赋值
        def __init__(self,cpu,board,ram,name='None'):
            self.cpu = cpu
            self.board = board
            self.ram = ram
            self.name = name

        def set_name(self,name):
            self.name = name

        #为PC类添加方法
        def get_para(self):
            print('hostname:%s\ncpu:%d\nboard:%s\nram:%d\n'%(self.name,self.cpu,self.board,self.ram))

        def drawing(self,object):
            ram_need = 2048
            if self.ram < ram_need:
                print("%s less of ram to drawing. %d at least!"%(self.name,ram_need))
            else:
                print('A '+object+' has been drawn!')
        def calculate(self,fun):
            res = fun()
            cpu_need = 4500
            if res < 100:
                print("%s calculate %s : %d"%(self.name,fun.__name__,res))
            else:
                if self.cpu < 4500:
                    print("%s's cpu can't support %s. at least %d"%(self.name,fun.__name__,cpu_need))
                else:
                    print("%s calculate %s : %d"%(self.name,fun.__name__,res))
    #类的继承
    class NOTEBOOK(PC):
        pass


    #创建两个pc对象pc01,pc02
    pc1 = PC(cpu=4400,board='board1',ram=4094)
    pc2 = PC(cpu=4900,board='board2',ram=1024)
    #通过方法打印pc的属性
    pc1.set_name('pc1')
    pc1.get_para()
    pc2.set_name('pc2')
    pc2.get_para()
    print('######################')
    #测试不同pc的绘图方法
    pc1.drawing('cat')
    pc2.drawing('dog')
    #测试不同pc的计算方法
    def fun01():
        return 10*9
    def fun02():
        return 10*11
    pc1.calculate(fun01)
    pc1.calculate(fun02)
    pc2.calculate(fun01)
    pc2.calculate(fun02)
    print('######################')
    #测试继承效果
    notebook01 = NOTEBOOK(cpu=4700,board='board3',ram=9600,name='note01')
    notebook01.get_para()

else:
    pass