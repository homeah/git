class Const:
    def __setattr__(self,name,value):
        if name in self.__dict__:
            raise TypeError('常量无法改变！')
        if not name.isupper():
            raise TypeError('常量必须大写！')

        self.__dict__[name] = value

import sys
sys.modules[__name__] = Const()
