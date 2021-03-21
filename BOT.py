n = int(input())
a = list(map(int,input().split()))

l = [a[0]]
maxx = l[0]
p = 1
q = 1
for i in range(1, n):
    if a[i] > a[i] + l[i-1]:
        l.append(a[i])
        p = i +1
    else:
        l.append(a[i] + l[i-1])
    if l[i] > maxx:
        maxx = l[i]
        q = i +1
if p > q:
    p = q
print(maxx,p,q)
# sua lai roi nha