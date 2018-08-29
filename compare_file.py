def compare_file(file1,file2):
      f1 = open(file1)
      f2 = open(file2)
      count = 0
      differ = []
      for each_line in f1:
            f2_line = f2.readline()
            count += 1
            if each_line != f2_line:
                  differ.append(count)
      f1.close()
      f2.close()
      return differ
file1 = input('请输入第一个文件名:')
file2 = input('请输入第二个文件名:')
differ = compare_file(file1,file2)
if len(differ)==0:
      print('两个文件一模一样')
else:
      print('两个文件有%d行不一样'% len(differ))
      for a in differ:
            print('第%d行不一样' % a)
