i = 1
x = 7
flag = 0
while x<1000:
     if (x%2==1) and (x%3==2):
          flag = 1
          i += 1
          print('阶梯数是：', x)
          x = 7*i
     else:
          i += 1
          x = 7* i
if flag == 0:
     print('1000范围内找不到该阶梯数！')     

