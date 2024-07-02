def positive_sum(arr):
    x=0
    for i in range(len(arr)):
        if arr[i]>0:
            x+=arr[i]
    return x
    
print(positive_sum([1,2,3,4,5]))    