n, m = map(int, input().split())
a = list(map(int, input().split()))
pref = [0]*(n+1)

for i in range(1,n+1):
    pref[i] = pref[i-1]+a[i-1] 

for i in range(m):
    l,s = map(int, input().split())
    L = -1
    R = n-l+1 

    while R-L > 1:
        mid = (L+R)//2
        if pref[mid+l]-pref[mid] <= s:
            L = mid 
        else:
            R = mid 
    
    if L+l <= n and pref[L+l]-pref[L] == s:
        print(L+1)
    else:
        print(-1)
