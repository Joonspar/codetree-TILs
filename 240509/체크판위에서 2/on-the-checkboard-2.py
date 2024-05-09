r,c = map(int,input().split())
mat = []
for _ in range(r):
        mat.append(list(map(str,input().split())))
# w -> b , b -> w
# 대각선만 가능
# 기회는 3번만 가능함 , 그 기회의 경우의수를 구하기
# i,j는 (0,0)보다 커야함. 즉, 1이상
# k,l은 i,j보다 커야함 
# mat[0][0] != mat[i][j] ....
answer = 0
for i in range(1,r-1):
    for j in range(1,c-1):
        for k in range(i+1,r-1):
            for l in range(j+1,c-1):
                if mat[0][0] != mat[i][j] and mat[i][j] != mat[k][l] and mat[k][l] != mat[-1][-1]:
                    answer += 1
print(answer)