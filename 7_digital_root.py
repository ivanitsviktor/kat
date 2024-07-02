def digital_root(n):
    s=0
    l=(str(n))
    if len(l)<2:
        return n
    for i in range(len(l)):
        s+=int(l[i])
    return digital_root(s)
    
  