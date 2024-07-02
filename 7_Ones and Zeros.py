def binary_array_to_number(arr):
    a=[]
    for i in arr:
       a.append(str(i)) 
    return int(''.join(a),2)
    
    
    
print(binary_array_to_number(  [1,1,1,1]))  