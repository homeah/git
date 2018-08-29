result = []
def getdigits(n):
     if n:
          result.insert(0,n%10)
          getdigits(n//10)


getdigits(244669452)
print(result) #直接打印结果
reverse = list(sorted(result))
print(reverse) #排序后打印结果
