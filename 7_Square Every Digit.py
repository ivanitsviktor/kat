def square_digits(num):
    s=''
    for i in range(len(str(num))):
        s+=str(int(str(num)[i])*int(str(num)[i]))
    return (s)
print(square_digits(9119))