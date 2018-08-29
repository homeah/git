'''
【程序26】 
题目：利用递归方法求5!。
1.程序分析：递归公式：fn=fn_1*4!
2.程序源代码：
'''
'''
def recursion(n):
    if n == 1:
        return n
    else:
        return n*recursion(n-1)
print('5!的结果是%d'%recursion(5))
'''

def recursion(n):
    return n if n==1 else n*recursion(n-1)
print('5!的结果是%d'%recursion(5))
