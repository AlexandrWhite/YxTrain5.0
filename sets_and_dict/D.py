n, k = map(int, input().split())
d = dict()
arr = list(map(int, input().split()))

ans = False 

for i in range(n):
    if arr[i] in d.keys():
        if i - d[arr[i]] <= k:
            ans = True
    d[arr[i]] = i 

if ans:
    print("YES")
else:
    print("NO")