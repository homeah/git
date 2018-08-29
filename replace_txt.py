def replacetxt(filename,old,new,newfilename):
      count = 0
      replacement = []
      f1 = open(filename)
      f2 = open(newfilename,'w')
      for each_line in f1:
            count += each_line.count(old)
            replacement.append(each_line.replace(old,new))

      print('%s有%d处\"%s\",需要替换成\"%s\"吗，请输入Yy/Nn：' %(filename,count,old,new),end ='')
      yes_or_no = input()
      if yes_or_no in 'Yy':
            f2.writelines(replacement)
            print('替换完毕，请打开%s查看' % newfilename)
      else:
            print('你输入的是N或者n，没有替换！')
      f1.close()
      f2.close()
filename = input('请输入要打开的文件名:')
old = input('请输入要被替换的内容：')
new = input('请输入新替换的内容：')
newfilename = input('请输入替换后要保存的文件名：')
replacetxt(filename,old,new,newfilename) 
      
