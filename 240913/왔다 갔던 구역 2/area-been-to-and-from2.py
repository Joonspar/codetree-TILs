n = int(input())
res = [0] * 2000
cur = 1001  # 시작점은 1001 (OFFSET 포함)

for _ in range(n):
    dis, dire = input().split()
    dis = int(dis)
    
    if dire == 'R':
        # 오른쪽으로 이동: cur + 1부터 cur + dis까지 칠하기
        for i in range(cur + 1, cur + dis + 1):
            res[i] += 1
        cur += dis  # 이동 후 위치 갱신
    else:
        # 왼쪽으로 이동: cur - 1부터 cur - dis까지 칠하기
        for i in range(cur - 1, cur - dis - 1, -1):
            res[i] += 1
        cur -= dis  # 이동 후 위치 갱신

# 2번 이상 지나간 영역의 크기 구하기
cnt = 0
for i in range(len(res)):
    if res[i] >= 2:
        cnt += 1

print(cnt)