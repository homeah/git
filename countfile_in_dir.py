def count_file_in_dir(directory):
    import os
    all_file = os.listdir(directory)
    dict1 ={}
    for each_file in all_file:
          if os.path.isdir(each_file):
                dict1.setdefault('文件夹',0)
                dict1['文件夹'] += 1
          else:
                ext = os.path.splitext(each_file)[1]
                dict1.setdefault(ext,0)
                dict1[ext] += 1
    print(dict1)
    for each in dict1.keys():
          print('%s目录下【%s】的文件类型有%d个' % (directory,each,dict1[each]))

directory = input('请输入要统计的目录：')
count_file_in_dir(directory)
            
            
