'''有1、2、3、4个数字，能组成多少个互不相同且无重复数字的三位数？都是多少？ '''
count = 0
list1 = []
for n1 in range(1,5):
    for n2 in range(1,5):
        for n3 in range(1,5):
            if (n1 != n2) and (n1 !=n3) and (n2 != n3):
                count += 1
                list1.append(n1*100+n2*10+n3)
print('共有%d个三位数，分别是：' %count)
for each in list1:
    print(each)

