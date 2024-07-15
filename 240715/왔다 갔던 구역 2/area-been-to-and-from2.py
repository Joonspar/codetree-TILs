n = int(input())
state = 10  # 초기 위치를 10으로 설정
arr = [0] * 100  # 위치를 기록할 배열, 충분히 큰 크기로 설정

for _ in range(n):
    cnt, direction = input().split()
    cnt = int(cnt)
    if direction == 'R':
        for i in range(1, cnt + 1):
            arr[state + i] += 1
        state += cnt
    elif direction == 'L':
        for i in range(1, cnt + 1):
            arr[state - i] += 1
        state -= cnt

# 2번 이상 지나간 영역의 크기 계산
overlapped_count = sum(1 for x in arr if x >= 2)
print(overlapped_count)