def libs():
    a = 0
    b = 1
    while True:
        a,b = b,a+b
        if a > 100:
            break
        yield a 
