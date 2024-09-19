# 보는 방향에 따라 순서가 달라짐
# i = 행 , j = 열? 그래서 i는 상하 j는 좌우
# 상하좌우에 특징이 있는지 ??
# 격자에서는 index가 존재하고 0부터 하는게 보통..임 ex ) 3행 2열은 (2,1)이 된다.
# 격자 , i,j이므로 x,y가 바뀜.
# 행이 아래로 갈때가 1이 추가 , 열이 오른쪽이 1 추가.
# 격자를 벗어나나? 
# 방지 : def in_range(x,y) : return 0<= x < 5 and 0<= y < 5
n = int(input())

def is_range(x,y):
    return 0<= x < n and 0<= y < n
rects = [
    list(map(int,input().split()))
    for _ in range(n)
]
ans = 0
dxs , dys = [0,1,0,-1] , [1,0,-1,0] 
for i in range(n):
    for j in range(n):
        cnt = 0
        for dx,dy in zip(dxs,dys):
            nx,ny = i + dx , j + dy
            if is_range(nx,ny) and rects[nx][ny] == 1:
                cnt += 1
        if cnt >= 3:
            ans += 1
print(ans)