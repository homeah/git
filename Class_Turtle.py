import random as r
legal_x = [0,10]
legal_y = [0,10]

class Turtle():
      def __init__(self):
            self.power = 100       #初始体力 
            self.x = r.randint(legal_x[0],legal_y[1]) #初始横坐标
            self.y = r.randint(legal_y[0],legal_y[1]) #初始纵坐标
            

      def move(self):
            #随机计算方向并移动到新的位置(x,y),乌龟一次只能沿着一个轴移动
            temp = r.choice(['x','y'])
            if temp == 'x':
                  new_x = self.x + r.choice([-2,-1,1,2])
                  new_y = self.y
            else:
                  new_y = self.y + r.choice([-2,-1,1,2])
                  new_x = self.x
            #检查是否超边界X轴
            if new_x > legal_x[1]:
                  self.x = legal_x[1]-(new_x -legal_x[1])
            elif new_x < legal_x[0]:
                  self.x = legal_x[0]-(new_x -legal_x[0])
            else:
                  self.x = new_x
            #检查是否超边界y轴
            if new_y > legal_y[1]:
                  self.y = legal_y[1]-(new_y -legal_y[1])
            elif new_y < legal_y[0]:
                  self.y = legal_y[0]-(new_y -legal_y[0])
            else:
                  self.y = new_y
            self.power -= 1
            return (self.x,self.y)

      def eat(self):
            self.power += 20
            if self.power > 100:
                  self.power = 100

class Fish:
      def __init__(self):
            self.x = r.randint(legal_x[0],legal_y[1]) #初始横坐标
            self.y = r.randint(legal_y[0],legal_y[1]) #初始纵坐标
      def move(self):
            #随机计算方向并移动到新的位置(x,y)
            temp = r.choice(['x','y'])
            if temp == 'x':
                  new_x = self.x + r.choice([-1,1])
                  new_y = self.y
            else:
                  new_y = self.y + r.choice([-1,1])
                  new_x = self.x

            #检查是否超边界X轴
            if new_x > legal_x[1]:
                  self.x = legal_x[1]-(new_x -legal_x[1])
            elif new_x < legal_x[0]:
                  self.x = legal_x[0]-(new_x -legal_x[0])
            else:
                  self.x = new_x
            #检查是否超边界y轴
            if new_y > legal_y[1]:
                  self.y = legal_y[1]-(new_y -legal_y[1])
            elif new_y < legal_y[0]:
                  self.y = legal_y[0]-(new_y -legal_y[0])
            else:
                  self.y = new_y
            return(self.x,self.y)

turtle = Turtle()
temp_tuple =(turtle.x,turtle.y)
print(temp_tuple)
print(turtle.move())
fish=[]
for i in range(10):
      new_fish = Fish()
      fish.append(new_fish)
while True:
      if not len(fish):
            print('鱼被吃光了！')
            break
      if not turtle.power:
            print('乌龟没力气啦！')
            break
      pos = turtle.move()
      for each in fish[:]:
            if each.move() == pos:
                  turtle.eat()
                  fish.remove(each)
                  print('有一条鱼被吃掉了！')


            

      
                                   
            
