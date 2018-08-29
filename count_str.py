str = input('请输入字符串：')
list1 = []
for each in str:
     if each not in list1:
          if each == '\n':
               print('\\n出现的次数是：',str.count(each))
          else:
               print(each,"出现的次数是：",str.count(each))
     list1.append(each)
          
     
