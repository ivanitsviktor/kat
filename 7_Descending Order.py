def descending_order(num):
    # print(type(num))
    # print(num)
    # print(int(''.join(list(reversed(sorted(list(str(num))))))))
    
    return int(''.join(list(reversed(sorted(list(str(num)))))))   
    
    
    

print(descending_order(145263))