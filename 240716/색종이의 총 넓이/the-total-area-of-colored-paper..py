OFFSET = 100

n = int(input())
A = [
    [0 for _ in range(210)]
    for _ in range(210)
]

for _ in range(n):
    x1,y1 = map(int,input().split())
    x1 += OFFSET
    y1 += OFFSET
    for i in range(x1,x1+8):
        for j in range(y1,y1+8):
            A[i][j] = 1

area = 0
for row in A:
    area += sum(row)

print(area)