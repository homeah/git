import math
def is_prime(number):
    if number > 1:
        if number == 2:
            return True
        if number % 2 == 0:
            return False
        for current in range(3,int(math.sqrt(number)+1),2):
            if number % current == 0:
                return False
        return True
    return False

def sum_prime(num):
    while True:
        if is_prime(num):
            yield num
        num -= 1
        if num== 1:
            raise StopIteration

total = 0
for each in sum_prime(2000000):
    total += each
print(total)

