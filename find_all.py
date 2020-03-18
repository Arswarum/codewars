def find_all(array, n):
    iter = 0
    ans =[]
    for x in array:
        if x == n:
            ans.append(iter)
        iter += 1
    return ans