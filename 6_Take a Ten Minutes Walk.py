def is_valid_walk(walk):
    return len(walk)==10 and walk.count('n')==walk.count('s') and walk.count('e')==walk.count('w')
    
    
    #determine if walk is valid
    pass




print(is_valid_walk(['n','s','n','s','n','s','n','s','n','s']))