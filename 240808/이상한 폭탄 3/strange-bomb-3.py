n,k = map(int,input().split())
bombs = []
cnts = []
for _ in range(n):
    bombs.append(int(input()))
max_bombs = [0] * 10000000
for i in range(n):
    cnt = 0
    for j in range(i+1,n):
        if bombs[i] == bombs[j] and (j-i) <= k:
            cnt += 1
    max_bombs[bombs[i]] += cnt
ans = max(max_bombs)
if sum(max_bombs) == 0:
    print(0)
else:
    for i in range(len(max_bombs)):
        if ans == max_bombs[i]:
            cnts.append(i)
    print(max(cnts))