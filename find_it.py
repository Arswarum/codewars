seq = [20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]
def find_it(seq):
    return [it for it in seq if seq.count(it) % 2 != 0][0]
print(find_it(seq))