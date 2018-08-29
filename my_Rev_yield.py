def myRev(string):
    length = len(string) - 1
    while True:
        if length>=0:
            yield string[length]
            length -= 1
        else:
            raise StopIteration
        
