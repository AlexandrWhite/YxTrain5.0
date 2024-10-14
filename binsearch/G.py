def sum_in_sq(i,j,k):
    t1 = dp[i][j+k]
    t2 = dp[i+k][j]
    t3 = dp[i][j] 
    #print("T1", t1)
    #print("T2", t2)
    #print("T3", t3)
    return dp[i+k][j+k] - t1 - t2 + t3

def check(i,j,k):
    if j-k<0 or j+2*k>m or i+3*k>n:
        return False

    top = sum_in_sq(i,j,k) == k**2
    center = sum_in_sq(i+k,j,k) == k**2
    bottom = sum_in_sq(i+2*k,j,k) == k**2

    left = sum_in_sq(i+k,j-k,k) == k**2
    right = sum_in_sq(i+k,j+k,k) == k**2

    #print([center,top,right,bottom,left])
    return center and top and right and bottom and left  

def f(x):
    for i in range(n):
        for j in range(m):
            if check(i,j,x):
                return True 
    return False 

n,m = map(int, input().split())
field = [None for i in range(n)]

hor = [0 for i in range(n)]
ver = [0 for i in range(m)]


dp = [[0 for j in range(m+1)] for i in range(n+1)]



for i in range(1,n+1):
    row = list(input())
    for j in range(1,m+1):
        if row[j-1] == '#': 
            dp[i][j] = dp[i-1][j-1] + hor[i-1] + ver[j-1] + 1
            hor[i-1] += 1
            ver[j-1] += 1
        else:
            dp[i][j] = dp[i-1][j-1] + hor[i-1] + ver[j-1]

#dp[i+1][j+1] - сумма до dp[i][j]

# for row in dp[1:]:
#     print(row[1:])


#print('aka',sum_in_sq(0,6,3))
#print(check(0,3,3))

L = 0
R = min(n,m)

while R - L > 1:
    mid = (L+R)//2
    if not f(mid):
        R = mid
    else:
        L = mid 

print(L)