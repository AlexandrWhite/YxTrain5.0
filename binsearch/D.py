def cnt_rows(words,w):
    '''
    сколько строк если разместить слова на ширине w
    '''
    rows = 1 
    cursor = 0

    for word in words:     
        if cursor+word <= w:
            cursor += word+1
        else:
            rows += 1
            cursor = word+1
    return rows 

def f(x):
    return abs(cnt_rows(a,x)-cnt_rows(b,w-x))

w,n,m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))



L = max(a)
R = w-max(b)

# for i in range(L,R+1):
#     print(i, f(i))
# print("---------")



while R-L > 1:
    mid = (L+R)//2
    k = 1
    while f(mid)==f(mid+k):
        k*=2
    if f(mid) > f(mid+k):
        L = mid
    else:
        R = mid 

#print(L,R)
ans = min(max(cnt_rows(a,R),cnt_rows(b,w-R)), max(cnt_rows(a,L),cnt_rows(b,w-L)))
print(ans)
