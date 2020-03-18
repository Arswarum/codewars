def invert(lst):
    res = []
    for num in lst:
        if num <= 0:
            res.append(abs(num))
        else:
            res.append(int('-' + str(num)))
    return res