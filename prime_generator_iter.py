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

def get_primes(number):
    while True:
        if is_prime(number):
            number = yield number  #首次none，再次需要send才能赋值?
        number += 1

def print_successive_primes(iteration,base = 10):
    prime_generator = get_primes(base)
    prime_generator.send(None)
    for power in range(iteration):
        print(prime_generator.send(base **power))


