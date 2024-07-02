def wave(people):
    a=[]
    i=0
    while i < (len(people)):
        if people[i]==' ':
            i+=1
        else:
            a.append(people[:i]+people[i].upper()+people[i+1:])
            i+=1
    return a
wave('a       b    ')    
        



