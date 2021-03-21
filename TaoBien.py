n,k = input().split()
n = int(n)
k = int(k)
def taoBien(n,i,k):
    
    if k ==0:
        return n
    print(3 - k,i,n)
    return taoBien(n,i+1,k-1) + taoBien(n*i,1,k-1)
print(taoBien(n,1,k))