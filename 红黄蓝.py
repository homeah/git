print('red\tyellow\tblue')
for red in range(0,4):
     for yellow in range(0,3):
          for blue in range(2,7):
               if red+yellow+blue == 8:
                    print(red,'\t',yellow,'\t',blue)
