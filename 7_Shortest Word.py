def find_short(s):
    
    x=s.split()
    z=len(x[0])
    for i in range(1,len(x)):
        if len(x[i])<z:
            z=len(x[i])
    return z

print(find_short("bitcoin take over the world maybe who knows perhaps"))







# "bitcoin take over the world maybe who knows perhaps"), 3)