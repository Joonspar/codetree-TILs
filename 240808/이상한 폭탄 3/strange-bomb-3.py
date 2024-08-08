n,k = map(int,input().split())
bombs = []
for _ in range(n):
    bombs.append(int(input()))
max_bombs = [0] * 10000000
for i in range(n):
    cnt = 0
    for j in range(i+1,n):
        if bombs[i] == bombs[j]:
            cnt += 1
    max_bombs[bombs[i]] += cnt
ans = max(max_bombs)
if sum(max_bombs) == 0:
    print(0)
else:
    print(max_bombs.index(ans))