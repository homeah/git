#没有采用return
result = ''
def Dec2Bin(dec):
     global result
     if dec:
         result += str(dec%2)
         Dec2Bin(dec//2)
Dec2Bin(10)
result = reversed(result)
temp = ''.join(result)
print(temp)
