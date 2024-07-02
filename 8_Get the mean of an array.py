def get_average(marks):
    s=0
    for i in marks:
        s+=i
    return int(s/len(marks))//1
print(get_average([2,5,13,20,16,16,10]))