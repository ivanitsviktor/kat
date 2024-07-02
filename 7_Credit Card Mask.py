def maskify(cc):
    if len(cc)>=4:
        x=[]
        for i in range(len(cc)-4):
            x.append('#')
       
        return ''.join(x)+cc[-4:]
    else:
        return cc
print(maskify('hgfdfgjkljhgdxsdghk'))

    