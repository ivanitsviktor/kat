def reverse_words(text):
    a=text.split(' ')
    print(a)
    b=[]
    c=''
    for i in a:
        b.append(i[::-1])
    
    return ' '.join(b)
reverse_words('The quick brown fox jumps over the lazy dog.')
    
    
    
    
    
    
    
    #   test.assert_equals(reverse_words('The quick brown fox jumps over the lazy dog.'), 'ehT kciuq nworb xof spmuj revo eht yzal .god')
    #     test.assert_equals(reverse_words('apple'), 'elppa')
    #     test.assert_equals(reverse_words('a b c d'), 'a b c d')
    #     test.assert_equals(reverse_words('double  spaced  words'), 'elbuod  decaps  sdrow')