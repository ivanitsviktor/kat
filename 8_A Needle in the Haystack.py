def find_needle(haystack):
    for i in range(len(haystack)):
        if "needle" == haystack[i]:
            return(str('found the needle at position ' +str(i)))
    
    
print(find_needle(['3', '123124234', None, 'needle', 'world', 'hay', 2, '3', True, False])    )
    
    
    
