class FileObject:
      '''给文件对象进行包装从而确认在删除时文件流关闭'''
      def __init__(self,filename):
            self.new_file = open(filename,'r+')
      def __del__(self):
            self.new_file.close()
            del self.new_file
            
