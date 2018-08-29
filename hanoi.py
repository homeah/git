def hanoi(n,x,y,z):
     if n == 1:
          print(x,'------->',z)
     else:
          hanoi(n-1,x,z,y) #将n-1个盘子移动到y柱
          print(x,'------->',z)#将第n个也就是最底下的大盘子移动到z柱
          hanoi(n-1,y,x,z)#将y柱上n-1个盘子移动到z柱
