temp = [23,34,45,5,656,33,'a',-10,'b',431,560]
tempb = []
for b in range(len(temp)):
     if type(temp[b])==int:
          tempb.append(temp[b])
print(tempb)
mini = 0
for a in tempb:
     if a<mini:
          mini = a
print(mini)
          
