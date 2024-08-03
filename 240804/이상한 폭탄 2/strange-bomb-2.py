n,k = map(int,input().split())
bombs = []
pung = []
for i in range(n):
    num = int(input())
    bombs.append(num)
bomb = False
for i in range(n):
    for j in range(i+1,n):
        if bombs[i] == bombs[j] and (j - i) <= k:
            bomb = True
            pung.append(bombs[i])

if bomb:
    print(max(pung))
else:
    print(-1)