class Container(list):
    def __init__(self,*arg):
        super().__init__(arg)
        self.count = [0 for x in arg]
    def __len__(self):
        return len(self.x)
    def __getitem__(self,index):
        self.count[index] += 1
        return super().__getitem__(index)
    def __setitem__(self,index,value):
        self.count[index] += 1
        super().__setitem__(index,value)
        
    def __delitem__(self,index):
        del self.count[index]
        super().__delitem__(index)
        
    def counter(self,index):
        return self.count[index]
    
    def append(self,element):
        self.count.append(0)
        super().append(element)
    def pop(self, index = -1):
        del self.count[index]
        return super().pop(index) #继承，其他几个也可以用继承
    
    def insert(self,index,value):
        self.count.insert(index,0)
        super().insert(index,value)
    def clear(self):
        self.count.clear()
        super().clear()
    def list(self):
        return list()
    def reverse(self):
        self.count.reverse()
        super().reverse()
