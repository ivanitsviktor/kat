def is_triangle(a, b, c):
    if a>0 and b>0 and c>0:
        if a+b>c and a+c>b and b+c>a:
            return a+b>c and a+c>b and b+c>a
        else:
            return False
    else:
        return False
print(is_triangle(-1, 2, 3))