def friend(x):
    name=[]
    s=list(x)
    for i in s:
        if len(i)==4:
            name.append(i)
    return name
    
    
    
    
    
    
print(friend(["Jimm", "Cari", "aret", "truehdnviegkwgvke", "sixtyiscooooool"]))    
    
    
    
    # test.assert_equals(friend(["Ryan", "Kieran", "Mark",]), ["Ryan", "Mark"])
    #     test.assert_equals(friend(["Ryan", "Jimmy", "abc", "d", "Cool Man"]), ["Ryan"])
    #     test.assert_equals(friend(["Jimm", "Cari", "aret", "truehdnviegkwgvke", "sixtyiscooooool"]), ["Jimm", "Cari", "aret"])