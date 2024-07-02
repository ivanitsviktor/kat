def series_sum(n):
    s=0
   
    for i in range (1,n+1):
        s+=1/(1+(3*(i-1))) 
            
    return "%.2f" %s  
print(series_sum(5)  )