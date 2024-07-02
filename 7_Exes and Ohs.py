def xo(s):
    s_new=s.lower()
    return s_new.count('x')==s_new.count('o')
    pass
print(xo("oOxx"))
