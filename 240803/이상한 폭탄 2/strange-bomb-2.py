n,k = map(int,input().split())
bombs = []
pair = []
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
                pair.append([a,b])
                break

if bomb:
    print(max(bombs[pair[0][0]:pair[0][1]]))
else:
    print(-1)