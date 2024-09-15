n = int(input())
rects = [
    [0 for _ in range(n*8)]
    for _ in range(n*8)
]
points = [
    list(map(int,input().split()))
    for _ in range(n)
]

for x,y in points:
    for i in range(x,x+8):
        for j in range(y,y+8):
            rects[i][j] = 1
cnt = 0
for elem in rects:
    for idx in elem:
        if idx == 1:
            cnt += 1
print(cnt)