# 입력 받기
N = int(input())
a1, b1, c1 = map(int, input().split())
a2, b2, c2 = map(int, input().split())

# 가능한 조합의 수를 계산
valid_count = 0

# 1부터 N까지의 모든 가능한 3자리 조합을 탐색
for i in range(1, N+1):
    for j in range(1, N+1):
        for k in range(1, N+1):
            # 첫 번째 조합과의 거리 체크
            if (min(abs(i - a1), N - abs(i - a1)) <= 2 and 
                min(abs(j - b1), N - abs(j - b1)) <= 2 and 
                min(abs(k - c1), N - abs(k - c1)) <= 2):
                valid_count += 1
            # 두 번째 조합과의 거리 체크
            elif (min(abs(i - a2), N - abs(i - a2)) <= 2 and 
                  min(abs(j - b2), N - abs(j - b2)) <= 2 and 
                  min(abs(k - c2), N - abs(k - c2)) <= 2):
                valid_count += 1

# 결과 출력
print(valid_count)