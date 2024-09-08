def fill_diagonal(n, m):
    # n x m 크기의 직사각형 배열 초기화
    result = [[0] * m for _ in range(n)]
    num = 1  # 채울 숫자

    # 대각선 채우기
    for diag in range(n + m - 1):
        # 대각선의 시작점 설정
        if diag < m:  
            # 열이 범위를 벗어나지 않으면 열에서 시작
            x, y = 0, diag
        else:  
            # 열이 범위를 벗어나면 행에서 시작
            x, y = diag - m + 1, m - 1

        # 위에서 아래로 채우기
        while x < n and y >= 0:
            result[x][y] = num
            num += 1
            x += 1
            y -= 1

    # 결과 출력
    for row in result:
        print(" ".join(map(str, row)))

# 입력 받기
n, m = map(int, input().split())

# 대각선으로 숫자 채우기
fill_diagonal(n, m)