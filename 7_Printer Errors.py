def printer_error(s):
    o=0
    r='nopqrstuvwxyz'
    for i in r:
        o+=s.count(i)
    return str(o)+'/'+str(len(s))
    
    
    
    
    
    
s="aaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbmmmmmmmmmmmmmmmmmmmxyz"  
print(printer_error(s))  