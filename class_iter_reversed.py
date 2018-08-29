class MyRev:
    def __init__(self,string):
        self.string = string
        self.length = len(string)
    def __iter__(self):
        return self
    def __next__(self):
        self.length -= 1
        if self.length < 0:
            raise StopIteration
        return self.string[self.length]
        
        
