def Narcissus():
     nar = []
     for each in range(100,1000):
          temp1 = each
          result = 0
          while temp1:
               temp = temp1 % 10
               temp1 //= 10
               result = result + temp**3
          if result == each:
               nar.append(result)
     print('所有水仙花数是:',nar)
               
