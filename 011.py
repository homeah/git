'''f1 = 1
f2 = 1
for i in range(1,21):
    print ('%12d %12d' % (f1,f2))
    if (i % 2) == 0:
        print( '')
    f1 = f1 + f2
    f2 = f1 + f2



'''
def fibn(n):
    if n<=2:
        return 1
    else:
        return fibn(n-2)+fibn(n-1)
