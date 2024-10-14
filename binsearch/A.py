def more(x):
    L = -1
    R = len(a)

    while R-L > 1:
        mid = (L+R)//2
        if a[mid] >= x:
            R = mid
        else:
            L = mid 
    return R 

def less(x):
    L = -1
    R = len(a)

    while R-L > 1:
        mid = (L+R)//2
        if a[mid] <= x:
            L = mid 
        else:
            R = mid 
    return L 


n = int(input())
a = list(map(int, input().split()))
a.sort()

k = int(input())
for i in range(k):
    L,R = map(int, input().split())
    print(less(R) - more(L) + 1,end=' ')
