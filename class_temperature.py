class C2F(float):
      def __new__(cls,temp):
            new_temp = temp*1.8 + 32
            return float.__new__(cls,new_temp)
      
