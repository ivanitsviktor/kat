def dig_pow(n, p):
    s=0
    for i in range(len(str((n)))):
      
        s+=(int(str(n)[i]))**p
      
        p+=1
        
    if s%n==0:
        return int(s/n)
    else:
        return -1





print(dig_pow(695,2))


# 46288 --> 4³ + 6⁴+ 2⁵ + 8⁶ + 8⁷ = 2360688 = 46288 * 51

# n = 695; p = 2 ---> 2 since 6² + 9³ + 5⁴= 1390 = 695 * 2