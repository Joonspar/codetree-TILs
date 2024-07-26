n, k = map(int, input().split())
arr = [''] * 10001  # 위치가 1부터 10000까지이므로 크기를 10001로 설정

for _ in range(n):
    state, point = input().split()
    state = int(state)
    arr[state] = point

max_cnt = 0

# 모든 시작 위치를 탐색
for i in range(1, 10001 - k):
    res = 0
    for j in range(i, i + k + 1):
        if arr[j] == 'G':
            res += 1
        elif arr[j] == 'H':
            res += 2
    max_cnt = max(max_cnt, res)

print(max_cnt)