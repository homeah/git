string = input('请输入一组字符串：')
length = len(string)
while length<3:
     string = input('请输入一组大于3个字符的字符串：')
     length = len(string)
for a in range(3,length-3):
     #密码必须是小写字符，并且左边3个字符和右边3个字符都必须是大写
     if string[a].isupper():
          continue
     if string[a-1].islower():
          continue
     if string[a-2].islower():
          continue
     if string[a-3].islower():
          continue
     if string[a+1].islower():
          continue
     if string[a+2].islower():
          continue
     if string[a+3].islower():
          continue
     print(string[a],end=" ")
