'''
【程序12】
题目：判断101-200之间有多少个素数，并输出所有素数。
1.程序分析：判断素数的方法：用一个数分别去除2到sqrt(这个数)，如果能被整除，
　　　　　　则表明此数不是素数，反之是素数。 　　　　　　
2.程序源代码：
'''
from math import sqrt
total = 0
leap = 1
for i in range(101,201):
    k = int(sqrt(i))+1
    for j in range(2,k):
        if i % j == 0:
            leap = 0
            break
    if leap == 1:
        total += 1
        print(i,end=' ')
        if total % 10 == 0:
            print('')
    leap = 1
print('')
print('101到201之间的素数共有%d个' %total)
