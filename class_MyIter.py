class MyIter:
    def __init__(self,*arg):
        self.x = [each for each in arg]
        self.length = len(arg)-1
        self.temp = -1
    def __iter__(self):
        return self
    def __next__(self):
        self.temp += 1
        if self.temp > self.length:
            raise StopIteration
        return self.x[self.temp]
