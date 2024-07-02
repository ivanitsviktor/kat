def solution(s):
    z=[]
    
    if len(s)%2==0:
        for i in range(int(len(s)/2)):
            z.append(s[i*2]+s[i*2+1])
    else:
        for i in range(int((len(s)-1)/2)):
            z.append(s[i*2]+s[i*2+1])
        z.append(s[-1]+'_')
    return z
       
   




print(solution('abcdef'))

# * 'abc' =>  ['ab', 'c_']
# * 'abcdef' => ['ab', 'cd', 'ef']