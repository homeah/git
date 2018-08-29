import os
def search_vedio(start_dir,target):
      os.chdir(start_dir)
      for each in os.listdir(os.curdir):
            if os.path.splitext(each)[1] in target:
                  vedio_list.append(os.getcwd()+os.sep+each+os.linesep)
            if os.path.isdir(each):
                  search_vedio(each,target)
                  os.chdir(os.pardir)
                  
start_dir = input('请输入要查找的目录：')
target = ['.mp4','.avi','.rmvb','.mkv']
program_dir = os.getcwd()
vedio_list = []
search_vedio(start_dir,target)
f = open(program_dir+os.sep+'vedio_list.txt','w')
f.writelines(vedio_list)
f.close()

      
