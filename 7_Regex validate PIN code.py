def validate_pin(pin):
    if (str(pin)).isdigit():
        if int(pin)>=0:
            if len(str(pin)) in [4,6]: 
                return True
            else:
                return False
    else:
        return False
    
print(validate_pin('1c1211'))