import math
def is_square(n): 
    if n<0:
        return False 
    else:
        print(math.sqrt(n))
        print(round(math.sqrt(n)))
        if math.sqrt(n)==round(math.sqrt(n)):
            return True
        else:
            return False
print(is_square(5))