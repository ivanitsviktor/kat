def merge_arrays(arr1, arr2):
    return sorted(list(set(arr1+arr2)))
    



    # a=arr1+arr2
    # print(a)
    # s=set(a)
    # print(s)
    # b=list(s)
    # print(b)
    # print(sorted(list(set(arr1+arr2))))

print(merge_arrays([5, -27, 6, 325, 12, 124, 601, 213, 23, -8, 25, 56, -100, -34,1,3,5,7,9,11,12], [1,2,3,4,5,10,12]))