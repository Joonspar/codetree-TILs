A = list(map(int,input().split()))
B = list(map(int,input().split()))
M = list(map(int,input().split()))

rects = [
    [0 for _ in range(2000)]
    for _ in range(2000)
]

for i in range(A[0],A[2]):
    for j in range(A[1],A[3]):
        rects[i][j] = 1
for i in range(B[0],B[2]):
    for j in range(B[1],B[3]):
        rects[i][j] = 1
for i in range(M[0],M[2]):
    for j in range(M[1],M[3]):
        rects[i][j] = 0
cnt = 0
for li in rects:
    for elem in li:
        if elem == 1:
            cnt += 1
print(cnt)