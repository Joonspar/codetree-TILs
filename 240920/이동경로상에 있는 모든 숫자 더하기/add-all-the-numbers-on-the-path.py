n,t = map(int,input().split())
s = list(input())
rects = [
    list(map(int,input().split()))
    for _ in range(n)
]
x,y = n//2 , n//2
dxs , dys = [0,1,0,-1] , [1,0,-1,0]
dir_num = 3
ans = rects[x][y]
for i in range(t):
    if s[i] == 'L':
        dir_num = (dir_num - 1) % 4
    elif s[i] == 'R':
        dir_num = (dir_num + 1) % 4
    elif s[i] == 'F':
        x , y = x + dxs[dir_num] , y + dys[dir_num]   
        if 0 <= x and x < n and y < n and 0 <= y:
            ans += rects[x][y]
        else:
            x,y = x - dxs[dir_num] , y - dys[dir_num]
print(ans)