def tribonacci(signature, n):
    if n==0:
        return []
    if n<4:
        return signature[:n]
    # res=signature
    for i in range (3,n):
        signature.append(signature[i-3]+signature[i-2]+signature[i-1])
    return signature     
    
