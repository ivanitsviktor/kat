
def order_weight(strng):
    a=sorted(strng.split())
    b=[]
    for i in a:
        s=0
        for j in range(len(i)):
            s+=int(i[j])
        b.append([i,s])
    sorted(b,key=sort2)
    b=(sorted(b,key=sort2))
    c=[]
    for y in b:
        c.append(y[0])
    print(' '.join(c))
    
def sort2(second):
    return  second[1]
         
    






print(order_weight("2000 10003 1234000 44444444 9999 11 11 22 123"))
# "11 11 2000 10003 22 123 1234000 44444444 9999" )