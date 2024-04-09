n = int(input())
arr1 = [
    [0 for _ in range(n)]
    for _ in range(n)
]
a = 1
for i in range(n):
    for j in range(n):
        arr1[i][j] = a
        a += 1

# 수정된 부분: 행과 열의 인덱스를 바꾸어서 출력
for i in range(n):
    for j in range(n):
        print(arr1[j][i], end=' ')
    print()