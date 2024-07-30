# 입력 처리
N, K = map(int, input().split())

# 바구니 정보를 저장할 리스트
baskets = []

# 각 바구니의 사탕 수와 위치를 입력 받음
for _ in range(N):
    candies, position = map(int, input().split())
    baskets.append((candies, position))

# 최대 사탕 개수를 저장할 변수
max_candy_count = 0

# 범위 [0, 100] 내의 모든 중심점 c를 탐색합니다.
for c in range(101):
    current_candy_count = 0
    left_bound = c - K
    right_bound = c + K
    
    # 각 바구니의 위치를 검사하여 구간에 포함되는 사탕의 수를 계산합니다.
    for candies, position in baskets:
        if left_bound <= position <= right_bound:
            current_candy_count += candies
    
    # 최대 사탕 개수를 갱신합니다.
    if current_candy_count > max_candy_count:
        max_candy_count = current_candy_count

# 결과 출력
print(max_candy_count)