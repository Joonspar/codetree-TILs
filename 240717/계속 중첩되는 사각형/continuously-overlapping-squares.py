OFFSET = 100

n = int(input())
A = [
    [0 for _ in range(210)]
    for _ in range(210)
]
for i in range(1,n+1):
    x1,y1,x2,y2 = map(int,input().split())
    x1 , x2 = x1 + OFFSET , x2 + OFFSET
    y1 , y2 = y1 + OFFSET , y2 + OFFSET
    if i % 2 == 1:
        for j in range(x1,x2):
            for k in range(y1,y2):
                A[j][k] = 'R'
    else:
        for j in range(x1,x2):
            for k in range(y1,y2):
                A[j][k] = 'B'
area = 0
for row in A:
    area += row.count('B')
print(area)