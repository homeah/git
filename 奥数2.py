n = 0
for i in range(1,7):
    for j in range(1,7):
        for k in range(1,7):
            if (i+j+k) == 6:
                n +=1
                print(i,j,k)
print('有%d种摆法。' %n)
               
                            


    
