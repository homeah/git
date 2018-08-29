def count(*para):
     length = len(para)
     for i in range(length):
          letter = 0
          space = 0
          digit = 0
          other = 0
          for each in para[i]:
               if each.isalpha():
                    letter += 1
               elif each.isdigit():
                    digit += 1
               elif each == ' ':
                    space += 1
               else:
                    other += 1
          print('第%d个字符串共有：英文字母%d个，数字%d个，空格%d个，其它字符%d个。'%(i+1,letter,digit,space,other))
count('I love you','you love me 3 times','i love you more than you love me')
