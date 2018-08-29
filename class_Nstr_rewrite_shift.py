class Nstr(str):
      def __lshift__(self,other):
            temp = self[:other]
            self = self[other:]
            self += temp
            return self
      def __rshift__(self,other):
            temp = self[-other:]
            self = self[:-other]
            self = temp + self
            return self
            
                  
