n,m = map(int,input().split())

rects = [
    [0 for _ in range(n)]
    for _ in range(n)
]

def in_range(x,y):
    return 0 <= x < n and 0 <= y < n

for _ in range(m):
    cnt = 0
    r,c = map(int,input().split())
    r -= 1
    c -= 1
    rects[r][c] = 1
    if in_range(r-1,c):
        if rects[r-1][c] == 1:
            cnt += 1
    if in_range(r+1,c):
        if rects[r+1][c] == 1:
            cnt += 1
    if in_range(r,c-1):
        if rects[r][c-1] == 1:
            cnt += 1
    if in_range(r,c+1):
        if rects[r][c+1] == 1:
            cnt += 1
    if cnt == 3:
        print(1)
    else:
        print(0)