# 입력 처리
N, H, T = map(int, input().split())
heights = list(map(int, input().split()))

# 최소 비용 초기화
min_cost = float('inf')

# 가능한 모든 구간을 탐색합니다.
for i in range(N - T + 1):
    current_cost = 0
    
    # 구간 내의 모든 밭의 높이를 H로 맞추기 위한 비용 계산
    for j in range(i, i + T):
        current_cost += abs(heights[j] - H)
    
    # 최소 비용 갱신
    min_cost = min(min_cost, current_cost)

# 결과 출력
print(min_cost)