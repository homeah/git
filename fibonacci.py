def fibonacci(n):
     temp0 = 0
     temp1 = 1
     if n<2:
          return n
     while n-2 >= 0:
          temp2 = temp0+temp1
          temp0 = temp1
          temp1 = temp2
          n -= 1
     return temp2
     
