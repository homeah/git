class Mydes:
    def __init__(self,initval,name):
        self.value = initval
        self.name = name

    def __get__(self,instance,owner):
        print('正在获取变量：',self.name)
        return self.value

    def __set__(self,instance,value):
        print('正在修改变量：',self.name)
        self.value = value

    def __delete__(self,instance):
        print('正在删除变量：',self.name)
        print('这个变量无法删除')

class Test:
    x = Mydes(10,'x')
