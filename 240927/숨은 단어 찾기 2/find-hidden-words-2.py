n,m = map(int,input().split())
boards = [
	list(input())
	for _ in range(n)
]
dxs, dys = [1, 1, 1, -1, -1, -1, 0, 0], [-1, 0, 1, -1, 0, 1, -1, 1]
def in_range(x,y):
	return 0<=x < n and 0<=y <m 

cnt = 0
for i in range(n):
	for j in range(m):
		if boards[i][j] != 'L':
			continue
		for dx , dy in zip(dxs,dys):
			cntE = 0
			curx = i
			cury = j
			while True:
				nx = curx + dx
				ny = cury + dy
				if in_range(nx,ny) == False:
					break
				if boards[nx][ny] != 'E':
					break
				cntE += 1
				curx = nx
				cury = ny
				if cntE == 2:
					cnt += 1
					break
print(cnt)