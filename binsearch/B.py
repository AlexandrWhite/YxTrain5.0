def s(k):
    x = k
    s1 = (k+1)*(x*(x+1)//2)
    s2 = x*(x+1)*(2*x+1)//6
    s3 = k*(1+k)//2
    return s1 - s2 + s3 - 1 

n = int(input())
L = -1
R = n+1

while R-L>1:
    mid = (L+R)//2
    if s(mid) <= n:
        L = mid
    else:
        R = mid 

print(L)
