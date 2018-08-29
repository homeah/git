import easygui as g
import os
import sys
file_path = g.fileopenbox(default = "*.txt")
with open(file_path) as f:
      title = os.path.basename(file_path)
      msg = '文件【%s】的内容如下：'% title
      text = f.read()
      temp = g.textbox(msg,title,text)
if text != temp:
      choice = g.buttonbox('监测到内容发生改变，请选择以下操作：','警告',('覆盖保存','放弃保存','另存为'))
      if choice == '覆盖保存':
            with open(file_path,'w') as f:
                  f.write(temp)
      elif choice == '放弃保存':
            pass
      elif choice =="另存为":
            another_path = g.filesavebox(default = '*.txt')
            if os.path.splitext(another_path)[1] != '.txt':
                  another_path += '.txt'
            with open(another_path,'w') as newfile:
                  newfile.write(temp)
      else:
            sys.exit(0)



            

