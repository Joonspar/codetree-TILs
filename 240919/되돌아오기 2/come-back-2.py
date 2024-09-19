s = list(input())
n = len(s)
dir_num = 3
dxs = [1,0,-1,0]
dys = [0,-1,0,1]
x,y = 0,0
time = 0
for i in range(n):
    if s[i] == 'L':
        dir_num = (dir_num - 1) % 4
        time += 1
    elif s[i] == 'R':
        dir_num = (dir_num + 1) % 4
        time += 1
    else:
        x = x + dxs[dir_num]
        y = y + dys[dir_num]
        time += 1

    if x == 0 and y == 0:
        print(time)
        exit()
print(-1)