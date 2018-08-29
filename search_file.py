def search_file(start_dir,target):
      import os
      os.chdir(start_dir)
      for each in os.listdir(os.curdir):
            if each == target:
                  print('你要找的目录是',os.getcwd()+os.sep+each)
            if os.path.isdir(each):
                  search_file(each,target)
                  os.chdir(os.pardir)
start_dir = input('请输入初始查询目录：')
target = input('请输入查询目标：')
search_file(start_dir,target)
