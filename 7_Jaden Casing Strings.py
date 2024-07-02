def to_jaden_case(string):
    s=[]
    for i in string.split(' '):
        s.append(i.capitalize())
    return ' '.join(s) 

print(to_jaden_case("How can mirrors be real if our eyes aren't real"))