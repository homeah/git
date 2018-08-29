listn = list()
for i in range(1,7):
    for j in range(1,7):
        for k in range(1,7):
            if (i+j+k) == 6:
                temp_list = [i,j,k]
                m=0
                if not len(listn):
                    listn.append(temp_list)
                else:
                    for n in range(len(listn)):          #变成列表，再变成集合来对比，如果在列表变成的每个集合里面，则不加到最终列表上
                        if set(temp_list) == set(listn[n]):
                            m=1
                            break
                    if not m:
                        listn.append(temp_list)
                            
print('有%d种摆法,分别是：' %len(listn))
for i in range(len(listn)):
    print(listn[i])
    
