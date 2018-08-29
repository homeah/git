def findstr(dest,src):
     count = 0
     length = len(dest)-1
     if src not in dest:
          print('在目标字符串中未找到这个字符!')
     for a in range(length):
          if dest[a] == src[0] and dest[a+1] == src[1]:
               count += 1
     print(src,'在目标字符中共出现',count,'次！')

dest = input('请输入目标字符串：')
src = input('请输入两个字符串：')
findstr(dest,src)
