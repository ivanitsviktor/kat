def solution(s):
    z=list(s)
    print(z)
    for i in range(len(s)):
        if z[i].isupper():
            z[i]=' '+z[i]
    return(''.join(z))
    
    
    
    
    
solution("helloWorld")    
    
    
    
#       "camelCasing"  =>  "camel Casing"
#       "identifier"   =>  "identifier"
#       ""             =>  ""