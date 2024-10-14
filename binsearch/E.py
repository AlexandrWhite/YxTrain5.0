def f(x):
    k  = (x-1)//2
    return 2*k*(1+k) + (x//2+1)
    

n = int(input())
L = 0
R = int(1e10)

while R-L > 1:
    mid = (L+R)//2
    if f(mid) >= n:
        R = mid
    else:
        L = mid 

if abs(f(L)-n) < abs(f(R)-n):
    y = L - (n- f(L))
    x = 1 + n - f(L)
else:
    y = R - (f(R)-n)
    x = 1+ f(R)-n

print(f"{y}/{x}")