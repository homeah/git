import math as m
class Point: 
      #def __init__(self,x=0,y=0):
      #	self.x = x
      #	self.y = y
      x=0
      y=0
      def __init__(self,x,y):
            self.x = x
            self.y =  y
      def getX(self):
            return self.x
      def getY(self):
            return self.y
class Line:
      def __init__(self,p1,p2):
            self.x = p1.getX()-p2.getX()
            self.y = p1.getY()-p2.getY()
            self.len = m.sqrt(self.x*self.x + self.y*self.y)
      def getlen(self):
            print(self.len)
x1 = float(input('请输入第一个点的横坐标x:'))
y1 = float(input('请输入第一个点的纵坐标y:'))
x2 = float(input('请输入第二个点的横坐标x:'))
y2 = float(input('请输入第二个点的纵坐标y:'))
p1 = Point(x1,y1)                      
p2 = Point(x2,y2)                       
line = Line(p1,p2)
line.getlen()
