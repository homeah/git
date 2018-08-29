def decTobin(dec):
     temp = []
     result = ''
     while dec:
          a = dec % 2
          dec //= 2
          temp.insert(0,a)
     for a in temp:
          result += str(a)
     result = int(result)
     return result
