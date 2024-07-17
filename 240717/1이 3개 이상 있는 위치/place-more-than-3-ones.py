n = int(input())

rects = [
    list(map(int,input().split()))
    for _ in range(n)
]
dxs = [0,0,-1,1]
dys = [1,-1,0,0]

def is_range(x,y):
    return 0 <= x < n and 0 <= y < n

ans = 0
for i in range(n):
    for j in range(n):
        # i와 j 주변에 1의 개수가 3개 이상이면 ans에 1을 더해줌
        cnt = 0
        for dx,dy in zip(dxs,dys):
            nx , ny = i +dx , j + dy
            if is_range(nx,ny) and rects[nx][ny] == 1:
                cnt += 1
        if cnt >= 3:
            ans += 1
print(ans)