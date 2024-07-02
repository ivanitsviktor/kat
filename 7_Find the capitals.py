def capitals(word):
    m=[]
    for i in range(len(word)):
        if word[i].isupper():
            m.append(i)
    return m