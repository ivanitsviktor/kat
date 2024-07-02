def to_query_string(data):
    s=[]
    for i in data:
        if type(data[i])==list:
            for j in data[i]:
                s.append(i+"="+str(j))
        else:
            s.append(i+'='+str(data[i]))
    return '&'.join(s)
                
        
    
    
    
    # return s

# print(to_query_string({ "bar": [2, 4], "foo": [1, 3] }))
print(to_query_string({ "a": "Z", "b": "Y", "c": "X", "d": "W", "e": "V", "f": "U", "g": "T" }))







#   to_query_string({ "bar": 2, "foo": 1 }),
#           "bar=2&foo=1"
#         )
#         test.assert_equals(
#           to_query_string({ "bar": [2, 4], "foo": [1, 3] }),
#           "bar=2&bar=4&foo=1&foo=3"
#         )
#         test.assert_equals(
#           to_query_string({ "a": "Z", "b": "Y", "c": "X", "d": "W", "e": "V", "f": "U", "g": "T" }),
#           "a=Z&b=Y&c=X&d=W&e=V&f=U&g=T"
#         )