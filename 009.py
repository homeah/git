import sys
encoding = 'UTF-8'
for i in range(8):
    for j in range(8):
        if (i+j)%2 ==0:
            print(chr(219),end = '')
            print(chr(219),end ='')
        else:
            print('  ',end ='')
    print('')
