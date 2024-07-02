def move_zeros(lst):
    s=lst.count(0)
    for i in range(s):
        lst.remove(0)
        lst.append(0)
    return lst
print(move_zeros([1, 2, 0, 1, 0, 1, 0, 3, 0, 1]))