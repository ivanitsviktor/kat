def narcissistic( value ):
    v=list(str(value))
    s=0
    for i in range(len(v)):
       s+=(int(v[i]))**len(v)
    if s==value:
        return True
    else:
        return False 
        
print(narcissistic(153))