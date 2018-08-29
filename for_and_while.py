def for_while(list1):
    it = iter(list1)
    while True:
        try:
            print(next(it))
        except StopIteration:
            break
