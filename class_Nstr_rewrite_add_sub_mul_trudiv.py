'''class Nstr(str):
      def __init__(self,arg):
            if isinstance(arg,str):
                  self.total = 0
                  for i in arg:
                        self.total += ord(i)
            else:
                  print('参数错误！')
      def __add__(self,other):
            return self.total+other.total
      def __sub__(self,other):
            return self.total-other.total
      def __mul__(self,other):
            return self.total * other.total
      def __truediv__(self,other):
            return self.total / other.total
            '''
#两种方法计算，字符ASC码加减乘除
class Nstr(int):
      def __new__(cls,arg):
            if isinstance(arg,str):
                  total = 0
                  for i in arg:
                        total += ord(i)
                  arg = total
            return int.__new__(cls,arg)
