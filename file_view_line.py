def file_view(filename,n):
      f = open(filename)
      (begin,end)=n.split(':')
      if begin == '':
            begin = '1'
      if end == '':
            end = '-1'
      if begin == '1' and end == '-1':
            prompt = '的全文是:'
      elif begin == '1':
            prompt = '从开始到第%s行是：' % end
      elif end =='-1':
            prompt = '从第%s行到结束的是：' % begin
      else:
            prompt = '从第%s行到第%s行的是：' % (begin,end)
      print('%s%s' %(filename,prompt))
      for a in range(int(begin)-1):
            f.readline()
      line = int(end) - (int(begin)-1)
      if line<0:
            print(f.read())
      else:
            for each_line in range(line):
                  print(f.readline(),end = '')
      f.close()
filename = input('请输入文件名：')
n = input('请输入要显示的行数，格式【:n，m:n，n:，:】:')
file_view(filename,n)
            
