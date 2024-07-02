def get_sum(a,b):
    if a==b:
        return a
    elif b<a:
        a,b=b,a
        return get_sum(a,b)
    else:
        s=0
        for i in range (b-a+1):
            s+=a+i
        return s
print(get_sum(-1,2))







# (1, 0) --> 1 (1 + 0 = 1)
# (1, 2) --> 3 (1 + 2 = 3)
# (0, 1) --> 1 (0 + 1 = 1)
# (1, 1) --> 1 (1 since both are same)
# (-1, 0) --> -1 (-1 + 0 = -1)
# (-1, 2) --> 2 (-1 + 0 + 1 + 2 = 2)