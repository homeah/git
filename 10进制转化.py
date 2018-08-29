q = True
while q:
     num = input('请输入一个整数，按Q结束程序：')
     if num!='Q':
          num = int(num)
          print( num,'的10进制转化成8进制是0o%o' % num)
          print(num,'的10进制转化成16进制是0x%x' % num)
          print(num,'的10进制转化成2进制是' , bin(num))
     else:
          break
                
