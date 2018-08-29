import os
import pickle
class Mydes:
    saved = []
    def __init__(self,name):
        self.name = name
        self.filename = self.name + '.pkl'

    def __get__(self,instance,owner):
        if self.name not in Mydes.saved:
            raise AttributeError('%s尚未赋值' % self.name)
        with open(self.filename,'rb') as f:
            value = pickle.load(f)
        return value

    def __set__(self,instance,value):
        #self.value = value 不需要，写到pickle文件里面
        with open(self.filename,'wb') as f:
            pickle.dump(value,f)
            Mydes.saved.append(self.name)

    def __delete__(self,instance):
        os.remove(self.filename)
        Mydes.saved.remove(self.name)
        



class Test:
    x = Mydes('x')
    y = Mydes('y')
