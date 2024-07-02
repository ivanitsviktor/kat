def pig_it(text):
    a=[]
    s=text.split()
    for i in s:
        if i.isalpha():
            i=i[1:]+i[0]+'ay'
            a.append(i)
        else:
            a.append(i)   
    return ' '.join(a)
            
            




print(pig_it('Pig latin is cool !'))
# pig_it('Pig latin is cool') # igPay atinlay siay oolcay
# pig_it('Hello world !')     # elloHay orldway !
# test.assert_equals(pig_it('Pig latin is cool'),'igPay atinlay siay oolcay')
# test.assert_equals(pig_it('This is my string'),'hisTay siay ymay tringsay')