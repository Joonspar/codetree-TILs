n,k = map(int,input().split())
bombs = []
for i in range(n):
    num = int(input())
    bombs.append(num)

bomb = False
for i in range(n):
    for j in range(i+1,n):
        if bombs[i] == bombs[j]:
            if (j - i) <= k:
                bomb = True
                a = i
                b = j
                break

if bomb:
    print(max(bombs[a:b+1]))
else:
    print(-1)