n = int(input())

rect = [
    [0 for _ in range(n*200)]
    for _ in range(n*200)
]

rects = [
    list(map(int,input().split()))
    for _ in range(n)
]
for x1,y1,x2,y2 in rects:
    for i in range(x1,x2):
        for j in range(y1,y2):
            rect[i][j] = 1
cnt = 0
for elem in rect:
    for idx in elem:
        if idx == 1:
            cnt += 1
print(cnt)