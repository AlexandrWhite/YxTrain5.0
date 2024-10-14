from collections import Counter

class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y 
    
    def __and__(self,other):
        return self.x * other.y - self.y * other.x 
    
    def __sub__(self, other):
        return Point(self.x - other.x,self.y-other.y)

    def __add__(self, other):
        return Point(self.x+other.x, self.y+other.y)

    def __str__(self) -> str:
        return f"p({self.x},{self.y})"

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    
    def __hash__(self) -> int:
        return hash((self.x,self.y))

def line_to_vec(p1: Point, p2: Point):
    return Point(p2.x-p1.x,p2.y-p1.y)

def sort_point_line(line):
    x1,y1,x2,y2 = line 
    line = [Point(x1,y1),Point(x2,y2)]
    line.sort(key = lambda p: (-p.y,-p.x))
    return line 

def is_equal_lines(line1,line2):
    v1 = line_to_vec(*line1)
    v2 = line_to_vec(*line2)
    if v1&v2 == 0:
        line1 = sort_point_line(line1)
        line2 = sort_point_line(line2)
        d = line1[0]-line2[0]
        return line1[1] == line2[1]+d 
    return False

n = int(input())
lines_A = [None for i in range(n)]
lines_B = [None for i in range(n)]

for i in range(n):
    x1,y1,x2,y2 = map(int, input().split())
    line = [Point(x1,y1),Point(x2,y2)]
    line.sort(key = lambda p: (-p.y,-p.x))
    lines_A[i] = line

for i in range(n):
    x1,y1,x2,y2 = map(int, input().split())
    line = [Point(x1,y1),Point(x2,y2)]
    line.sort(key = lambda p: (-p.y,-p.x))
    lines_B[i] = line


d_dict = dict()
ans = 0 
for i in range(n):
    #print("LINE: ", lines_B[i])
    for j in range(n):
        v1 = line_to_vec(*lines_B[i])
        v2 = line_to_vec(*lines_A[j])
        if v1&v2 == 0:
            line1 = lines_B[i]
            line2 = lines_A[j]
            d = line1[0]-line2[0]
            if line1[1] == line2[1]+d:
                #print(lines_A[j])
                if d not in d_dict.keys():
                    d_dict[d] = 1 
                else:
                    d_dict[d] += 1

#print(d_dict)

if d_dict:
    mx = 0
    mx_key = 0
    for d in d_dict.keys():
        if d_dict[d] > mx:
            mx = d_dict[d]
            mx_key = d
    
    d = mx_key

    #print(d)

    ans = 0 
    for line in lines_A:
        p1,p2 = line
        p1 = p1+d 
        p2 = p2+d 
        if [p1,p2] not in lines_B:
            ans += 1
    print(ans)
else:
    print(n)
