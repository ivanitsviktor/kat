def filter_list(l):
    a=[]
    for i in l:
        if type(i)==int:
            a.append(i)
    return a        
        
        

print(filter_list([1, 2, 'a', 'b']))

     