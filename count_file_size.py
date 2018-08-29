import os
all_file = os.listdir(os.curdir)
dict1 = dict()
for each_file in all_file:
      if os.path.isfile(each_file):
            dict1[each_file] = os.path.getsize(each_file)
for each in dict1.items():
      print('当前目录下【%s】的大小是%s字节' %(each[0],each[1]))

            
            
      
      
