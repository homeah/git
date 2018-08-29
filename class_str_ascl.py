class Int_to_ASC(int):
      def __new__(cls,arg):
            if  isinstance(arg,str):
                  total = 0
                  for each in arg:
                        total += ord(each)
                  arg = total
            return int.__new__(cls,arg)      
