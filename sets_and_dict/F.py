P = int(1e9+7)
X = 2571

def hash(s):
    h = 0 
    x = 1 
    for i in range(len(s)):
        h = (h*x + ord(s[i]))%P
        x = (x*X)%P  
    return h

d = input().split()
d = dict(zip(map(hash,d),d))


words = input().split()
for word in words:

    ans = None 
    h = 0
    x = 1
    
    for i in range(len(word)):
        h = (h*x + ord(word[i]))%P
        x = (x*X)%P  
        if h in d.keys():
            ans = d[h]
            break

    if ans is not None:
        print(ans, end=' ')
    else:
        print(word, end=' ')       