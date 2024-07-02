def rgb(r, g, b):
    if r<0:
        r=0
    if r>255:
        r=255
    if g<0:
        g=0
    if g>255:
        g=255
    if b<0:
        b=0
    if b>255:
        b=255
    if len(str(hex(r)[2:]))==1:
        rr='0'+str(hex(r)[2:])
    else:
        rr=str(hex(r)[2:])
    if len(hex(g)[2:])==1:
        gg='0'+str(hex(g)[2:])
    else:
        gg=str(hex(g)[2:]) 
    if len(hex(b)[2:])==1:
        bb='0'+str(hex(b)[2:])
    else:
        bb=str(hex(b)[2:])   
    return ((rr+gg+bb).upper())
        
print(rgb(1, 275, 125))









# test.assert_equals(rgb(0, 0, 0), "000000", "testing zero values")
#         test.assert_equals(rgb(1, 2, 3), "010203", "testing near zero values")
#         test.assert_equals(rgb(255, 255, 255), "FFFFFF", "testing max values")
#         test.assert_equals(rgb(254, 253, 252), "FEFDFC", "testing near max values")
#         test.assert_equals(rgb(-20, 275, 125), "00FF7D", "testing out of range values")