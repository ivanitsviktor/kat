def check(seq, elem):
    if str(elem) in seq:
        return True
    elif elem in seq:
        return True
    else:
        return False
            
    
    
    
    
    
    
    
    
    #   (True, ([66, 101], 66)),
    #         (False, ([78, 117, 110, 99, 104, 117, 107, 115], 8)),
    #         (True, ([101, 45, 75, 105, 99, 107], 107)),
    #         (True, ([80, 117, 115, 104, 45, 85, 112, 115], 45)),