import easygui as g
import os
import io
import sys

def find_code(start_dir,target):
      os.chdir(start_dir)
      for each_file in os.listdir(os.curdir):
            ext = os.path.splitext(each_file)[1]
            if ext in target:
                  localdir = os.getcwd()
                  localfile = localdir+os.sep+each_file
                  code_file_list.append(localfile)
            if os.path.isdir(each_file):
                  find_code(each_file,target)
                  os.chdir(os.pardir)
      print(code_file_list)
      return code_file_list

def calc_lines(file):
      with open(file,'rb') as f:  #以二进制打开，避免了UnicodeDecodeError
            lines = 0
            for each in f:
                  lines += 1
            #print(f.read().decode('utf-8')) //重点关注解码，把二进制转化成可读
      return lines

def calc_total(code_file_list):
      total_lines = 0
      for each in code_file_list:
            lines = calc_lines(each)
            total_lines += lines
      title = '统计结果'
      msg = '您目前共累计写了%d行代码，完成进度：%.2f %%\n离10万行代码还差%d 行，请继续努力！'%(total_lines,total_lines/1000,10000-total_lines)
      g.msgbox(msg,title)
code_file_list=[]
start_dir = g.diropenbox('请选择你的代码库')
target = ['.py','.cc']
list_code = find_code(start_dir,target)
calc_total(list_code)
