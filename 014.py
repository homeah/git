'''
【程序14】
题目：将一个正整数分解质因数。例如：输入90,打印出90=2*3*3*5。

程序分析：对n进行分解质因数，应先找到一个最小的质数k，然后按下述步骤完成： 
(1)如果这个质数恰等于n，则说明分解质因数的过程已经结束，打印出即可。
(2)如果n<>k，但n能被k整除，则应打印出k的值，并用n除以k的商,作为新的正整数你n,
　重复执行第一步。
(3)如果n不能被k整除，则用k+1作为k的值,重复执行第一步。

2.程序源代码：
'''
from math import sqrt 


def depart(n):
    print('%d = '%n,end='')
    for i in range(2,n+1):
        while n!=i:
            if n%i == 0:
                print("%d * "%i,end='')
                n = n/i
            else:
                break
    print(int(n))
                

'''def depart(n):
    nums=[]
    k = n
    i = 2
    while i < (int(sqrt(k))+1):
        if k%i == 0:
            nums.append(i)
            k = k/i
            if k<4:
                break
            i=2  
        else:
            i += 1

    nums.append(k)
    if n==k:
        print('%d = %d'%(n,n))
    else:
        print('%d = ' %n,end ='')
        for each in range(len(nums)-1):
            print('%d * '%nums[each],end ='')
        print('%d'%nums[-1])
        '''
    
    
