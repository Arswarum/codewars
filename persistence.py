def persistence(n):
    counter = 0
    while n > 9:
        counter += 1
        n_str = str(n)
        total = 1
        for i in n_str:
            total *= int(i)
        n = total
    return counter