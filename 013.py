'''
【程序13】
题目：打印出所有的“水仙花数”，所谓“水仙花数”是指一个三位数，其各位数字立方和等于该数
　　　本身。例如：153是一个“水仙花数”，因为153=1的三次方＋5的三次方＋3的三次方。
1.程序分析：利用for循环控制100-999个数，每个数分解出个位，十位，百位。
2.程序源代码：
'''
print('水仙花数是：')
for i in range(100,1000):
    m = i % 10
    n = (i //10)%10
    k = i //100
    if m**3+n**3+k**3 == i:
        print(i,end = ' ')
