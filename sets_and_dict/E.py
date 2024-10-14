n1 = int(input())
arr1 = list(map(int,input().split()))

n2 = int(input())
arr2 = list(map(int,input().split()))

n3 = int(input())
arr3 = list(map(int,input().split()))

s1 = set(arr1)
s2 = set(arr2)
s3 = set(arr3)
s4 = list(set(arr1+arr2+arr3))
s4.sort()

for e in s4:
    c = 0
    if e in s1:
        c+=1
    if e in s2:
        c+=1
    if e in s3:
        c+=1
    if c > 1:
        print(e,end=' ')
