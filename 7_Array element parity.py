def solve(arr):
    for i in range(len(arr)):
        if arr[i]*(-1) not in arr:
            return arr[i]