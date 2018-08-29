def file_view(filename,n,new_file):
      f1 = open(filename)
      f2 = open(new_file,'w')
      for i in range(n):
            f2.write(f1.readline())
      f1.close()
      f2.close()
      
filename = input('请输入要打开的文件：')
n= int(input('请输入要读取的行数：'))
new_file = input('请输入写入的文件名：')
file_view(filename,n,new_file)
