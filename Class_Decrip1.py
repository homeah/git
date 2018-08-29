import time
class Mydes:
    def __init__(self,initval,name):
        self.value = initval
        self.name = name
        self.filename = '%s_record.txt' %self.name

    def __get__(self,instance,owner):
        with open(self.filename,'a', encoding='utf-8') as f:
            f.write('%s变量于北京时间 %s 被读取，%s = %s\n' \
                    %(self.name,time.ctime(),self.name,str(self.value)))
        return self.value

    def __set__(self,instance,value):
        self.value = value
        with open(self.filename,'a', encoding='utf-8') as f:
            f.write('%s变量于北京时间 %s 被修改，%s = %s\n' \
                    %(self.name,time.ctime(),self.name,str(self.value)))
        



class Test:
    x = Mydes(10,'x')
    y = Mydes(8.8,'y')
