n = int(input())
points = [None for i in range(n)]

for i in range(n):
    a,b = map(int, input().split())
    points[i] = (a,b)

x1,y1 = points[0]
best_ans = [(x1+1,y1),(x1,y1+1),(x1+1,y1+1)]

points_set = set(points)

for p1 in points:
    for p2 in points:
        if p1 != p2:
            ans = []
            x1,y1 = p1 
            x2,y2 = p2
            if abs(x1-x2) == abs(y1-y2):
                p3 = (x2,y1)
                p4 = (x1,y2)
            else:
                p3 = (x2-(y1-y2),y2+(x1-x2))
                p4 = (x1-(y1-y2),y1+(x1-x2))
            if p3 not in points_set:
                ans.append(p3)
            if p4 not in points_set:
                ans.append(p4) 

            if len(ans)<len(best_ans):
                best_ans = ans 
                
print(len(best_ans))
for point in best_ans:
    print(*point)
