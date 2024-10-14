# НЕ РЕШЕНА !!!
INF_p = int(1e9+1)
INF_n = int(-1e9-1)


def check(X):
    if X == 0:
        return False 
    
    for i in range(n):

        #print(f"INTERVAL L:{L} R:{R-1}")
        
        t2 = 0
        if i+X >= n:
            t2 = n-1
        else:
            L = i-1 
            R = n

            while R-L > 1:
                mid = (L+R)//2
                if points[mid][0] >= points[i][0]+X:
                    R = mid
                else:
                    L = mid 
            t2 = R

        t1 = i
        
        # 
        # найдем макс и мин на точках не доходящих до t1
        # найдем макс и мин на точках от t2 включительно и до конца

        #print("T1: ",t1)
        #print("T2: ",t2)
    
        max1, min1 = max_min_pref[t1]
        max2, min2 = max_min_suff[t2]
        #print(max_min_pref[t1+1])
        #print(max_min_suff[t2])

        y_max = max(max1,max2)
        y_min = min(min1,min2)

        #print(f"Y_MIN: {y_min}\nY_MAX: {y_max}")

        #значит покрыли все точки вертикальной линией
        if y_max == INF_n and y_min == INF_p: 
            return True 
        
        #значит есть возможность покрыть непокрытые точки горизонтальной линией 
        if y_max - y_min + 1 <= X:
            return True
    return False 



with open('input.txt', 'r') as f:
    w,h,n = map(int, f.readline().split())

    points = [None for i in range(n)]
    max_min_pref = [[INF_n, INF_p]  for i in range(n+1)]
    max_min_suff = [[INF_n, INF_p]  for i in range(n+1)]

    for i in range(n):
        x,y = map(int, f.readline().split())
        points[i] = (x,y) 

    #print("end input")

points.sort(key=lambda x: x[0])
#print(points) 

for i in range(n):
    x,y = points[i]
    max_min_pref[i+1][0] = max(max_min_pref[i][0], y) 
    max_min_pref[i+1][1] = min(max_min_pref[i][1], y)

for i in range(n-1,-1,-1):
    x,y = points[i]
    max_min_suff[i][0] = max(max_min_suff[i+1][0], y) 
    max_min_suff[i][1] = min(max_min_suff[i+1][1], y)

L = 0
R = min(w,h)+1

while R-L > 1:
    mid = (L+R)//2
    if check(mid):
        R = mid 
    else:
        L = mid
    #print('iter')  

print(R)
