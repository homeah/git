import os
def search_vedio(start_dir,target):
      os.chdir(start_dir)
      #all_files = os.walk(os.getcwd())
      all_files = os.walk(start_dir)
      vedio_list = []
      for each in all_files:
            for each_file in each[2]:
                  if os.path.splitext(each_file)[1] in target:
                        vedio = each[0]+os.sep+each_file+os.linesep
                        #vedio = os.path.join(each[0],each_file)
                        vedio_list.append(vedio)
      return vedio_list
directory = os.path.join(os.getcwd(),'vedio.list.txt')
start_dir = input('请输入起始目录：')
target = ['.mkv','.rmvb','.avi','.mp4']
vedio_list = search_vedio(start_dir,target)
f = open(directory,'w')
f.writelines(vedio_list)
f.close()
                        
