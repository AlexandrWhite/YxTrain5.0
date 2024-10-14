n = int(input())
arr = list(map(int,input().split()))
cnt = [0 for i in range(int(1e5+1))]

for ai in arr:
    cnt[ai]+=1

mx = 0
for i in range(int(1e5)):
    mx = max(mx, cnt[i]+cnt[i+1])
print(n-mx)