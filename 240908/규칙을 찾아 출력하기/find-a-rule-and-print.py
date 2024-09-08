n = int(input())
arr = [['*' for _ in range(n)] for _ in range(n)]

# 각 줄의 패턴을 조정
for i in range(1, n-1):
    for j in range(i, n-1):
        arr[i][j] = ' '

# 배열 출력
for li in arr:
    print(' '.join(li))