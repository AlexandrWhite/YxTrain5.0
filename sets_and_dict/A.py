n = int(input())
d = dict()

for i in range(n):
    k = int(input())
    songs = input().split()
    for song in songs:
        if song in d.keys():
            d[song] += 1
        else:
            d[song] = 1

best_songs = []
for song in d.keys():
    if d[song] == n:
        best_songs.append(song)

best_songs.sort()
print(len(best_songs))
print(*best_songs)

