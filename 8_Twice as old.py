def twice_as_old(dad_years_old, son_years_old):
    i=0
    while dad_years_old-son_years_old!=i:
        i+=1
    if (son_years_old-i)<0:
        return i-son_years_old
    else:
        return son_years_old-i


twice_as_old(29,0)






# test.assert_equals(twice_as_old(36,7) , 22)
#         test.assert_equals(twice_as_old(55,30) , 5)
#         test.assert_equals(twice_as_old(42,21) , 0)
#         test.assert_equals(twice_as_old(22,1) , 20)
#         test.assert_equals(twice_as_old(29,0) , 29)