import os
def pos_in_line(line,key): #一行中找到关键字符位置，位置可能不止一个，返回位置列表
      pos = []
      begin = line.find(key)
      while begin != -1:
            pos.append(begin+1)
            begin = line.find(key,begin+1)
      return pos

def search_in_file(file_name,key): #在文件中每行去找关键字，返回字典【行:位置】
      f = open(file_name)
      count = 0
      key_dict = dict()
      for each_line in f:
            count += 1
            if key in each_line:
                  pos = pos_in_line(each_line,key)
                  key_dict[count] = pos
      f.close()
      return key_dict

def search_files(key,directory): #搜索出当前目录（含子目录）下，所有txt文件，再找key
      os.chdir(directory)
      all_files  = os.walk(os.getcwd())
      txt_file = []
      for i in all_files:
            for each_file in i[2]: #每个目录下文件
                  if os.path.splitext(each_file)[1] == '.txt':
                        each_file = os.path.join(i[0],each_file)
                        txt_file.append(each_file)
      for each_txt_file in txt_file:
            key_dict = search_in_file(each_txt_file,key)
            if key_dict:
                  print('==================================')
                  print('在%s中找到%s' %(each_txt_file,key))
                  for each_dict in key_dict.items():
                        print('具体在%s行第%s个位置出现' %(each_dict[0],each_dict[1]))
key = input('请输入要查找的关键字符：')
directory = input('请输入要查找的路径：')
search_files(key,directory)

                  
      
            
