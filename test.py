for i in range(100,999):
     x = int(i/100)
     y = int((i%100)/10)
     z = (i%100)%10
     if i == x**3 + y**3 + z**3 :
          print(i)