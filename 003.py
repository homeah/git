'''一个整数，它加上100后是一个完全平方数，再加上168又是一个完全平方数，请问该数是多少？'''
import math
for i in range(1,100000):
    x = int(math.sqrt(i+100))
    y = int(math.sqrt(i+168))
    if x*x==(i+100) and y*y == (i+168):
        print(i)
