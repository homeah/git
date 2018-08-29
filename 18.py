'''
题目：求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。例如2+22+222+2222+22222(此时
　　　共有5个数相加)，几个数相加有键盘控制。
1.程序分析：关键是计算出每一项的值。
2.程序源代码：
'''
from functools import reduce
Tn = 0
Sn = []
#total = 0
n = int(input('请输入连加几位数:'))
a = int(input('请输入一个数字:'))
for count in range(n):
    Tn += a
    a *= 10
    Sn.append(Tn)
    #total += Tn 
    print(Tn)
#print(total)
Sn = reduce(lambda x,y :x+y,Sn) #主要展示下lambda,和reduce用法
print(Sn)
