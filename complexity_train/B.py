g1,g2 = map(int,input().split(":"))
x1,x2 = map(int,input().split(":"))
home = int(input())

d = g2+x2-g1-x1


if d >= 0:
    #проигрывает или ничья у первой команды
    x1+=d
    guest_1 = g1 if home==2 else x1
    guest_2 = x2 if home==2 else g2
    if guest_1 <= guest_2:
        d+=1
else:
    d = 0

print(d)