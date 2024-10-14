def get_ans(t1,t2):
    if(max(t1,t2)<0):
        print("NO")
    else:
        print("YES")
        ans = min(t1,t2) if min(t1,t2)>0 else max(t1,t2)
        print(f"{ans:.{15}f}")

def best(x1,v1,x2,v2):
    k = 0
    t = (x1+x2-k*L)/(-v1-v2)
    if -v1-v2 < 0:
        k = (x1+x2+L-1)//L
        t = (x1+x2-k*L)/(-v1-v2)
    if -v1-v2 > 0 and t<0:
        k = -(x1+x2+L-1)//L
        t = (x1+x2-k*L)/(-v1-v2)
    return t

def best2(x1,v1,x2,v2):
    k = 0
    t = (x2-x1-k*L)/(v1-v2)
    if v1-v2 < 0:
        k = (x2-x1+L-1)//L
        t = (x2-x1-k*L)/(v1-v2)
    if v1 - v2 > 0 and t<0:
        k = -(x2-x1+L-1)//L
        t = (x2-x1-k*L)/(v1-v2)
    return t

L, x1,v1,x2,v2 = map(int, input().split()) 

if(x1 == x2):
    print("YES\n0")
    quit()

if v1 ==0 and v2 ==0:
    print("NO")
elif v1 == 0 or v2 == 0:
    t1 = -1 if v1+v2 == 0 else (L-x1-x2)/(v1+v2)
    t2 = min(best(x1,v1,x2,v2),best2(x1,v1,x2,v2))
    get_ans(t1,t2)
else:
    t1 = -1 if -v1-v2 == 0 else best(x1,v1,x2,v2)
    t2 = -1 if v1-v2 == 0 else best2(x1,v1,x2,v2)
    get_ans(t1,t2)
