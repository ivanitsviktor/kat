def tower_builder(n_floors):
    a=[]
    for i in range(0,n_floors):
        a.append(' '*(n_floors-1-i)+'*'*(2*i+1)+' '*(n_floors-1-i))
    return(a)
    
tower_builder(4)    
    
    
    
    
    
    
    
    
    #  test.assert_equals(tower_builder(3), ['  *  ', ' *** ', '*****'])