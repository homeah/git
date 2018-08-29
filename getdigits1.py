# 'NoneType' object has no attribute 'append'
def getdigits(n):
     result = []
     if n:
          result = getdigits(n//10)
          return result.append(n%10) 
     else:
          return result


getdigits(244669452)
print(result) #直接打印结果
reverse = list(sorted(result))
print(reverse) #排序后打印结果
