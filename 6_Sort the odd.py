def sort_array(source_array):
    m=[]
    for i in range(len(source_array)):
        if source_array[i]%2==1:
            m.append(source_array[i])
            source_array[i]='x'
    m.sort()
    j=0
    for i in range(len(source_array)):
        if source_array[i]=='x':
            source_array[i]=m[j]
            j+=1
    return source_array
sort_array([2, 22, 37, 11, 4, 1, 5, 0])










#   test.assert_equals(sort_array([5, 3, 2, 8, 1, 4]), [1, 3, 2, 8, 5, 4])
#         test.assert_equals(sort_array([5, 3, 1, 8, 0]), [1, 3, 5, 8, 0])
#         test.assert_equals(sort_array([]),[])
#         test.assert_equals(sort_array([5, 3, 2, 8, 1, 4, 11]), [1, 3, 2, 8, 5, 4, 11])
#         test.assert_equals(sort_array([2, 22, 37, 11, 4, 1, 5, 0]), [2, 22, 1, 5, 4, 11, 37, 0])