def row_sum_odd_numbers(n):
    m=(1+n)/2*n
    sm=(2+(m-1)*2)/2*m
    sn=(2+(m-n-1)*2)/2*(m-n)
    return int((2+((1+n)/2*n-1)*2)/2*(1+n)/2*n-(2+((1+n)/2*n-n-1)*2)/2*((1+n)/2*n-n))




print(row_sum_odd_numbers(41))