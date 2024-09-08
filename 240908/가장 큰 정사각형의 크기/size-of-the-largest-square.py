def largest_square_area(n, m, grid):
    # DP 테이블 초기화
    dp = [[0] * m for _ in range(n)]
    max_side = 0

    # 첫 번째 행과 열 초기화
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 1:
                if i == 0 or j == 0:
                    dp[i][j] = 1  # 첫 번째 행이나 열에서는 정사각형 변의 길이가 1
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                max_side = max(max_side, dp[i][j])

    return max_side * max_side

# 입력 받기
n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# 가장 큰 정사각형의 넓이 출력
print(largest_square_area(n, m, grid))