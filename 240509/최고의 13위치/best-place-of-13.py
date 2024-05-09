n = int(input())
mat = []
for _ in range(n):
    mat.append(list(map(int,input().split())))
cnt = 0
for i in range(n):
    for j in range(n-2):
        cnt = max(cnt,mat[i][j+2] + mat[i][j+1] + mat[i][j])
print(cnt)