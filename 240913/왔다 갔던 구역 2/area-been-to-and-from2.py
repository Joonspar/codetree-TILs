OFFSET = 1000  # 음수 좌표를 다루기 위한 오프셋
MAX_R = 20002   # 최대 좌표 범위 설정

# 입력 처리
n = int(input())  # 명령의 개수
res = [0] * (MAX_R + 1)  # 지나간 구간을 기록할 배열
cur = OFFSET  # 시작점은 OFFSET을 기준으로 0

for _ in range(n):
    dis, dire = input().split()
    dis = int(dis)

    if dire == 'R':
        # 오른쪽으로 이동: cur + 1부터 cur + dis까지
        for i in range(cur+1, cur + dis):
            res[i] += 1
        cur += dis  # 현재 위치 갱신
    else:
        # 왼쪽으로 이동: cur - 1부터 cur - dis까지
        for i in range(cur, cur - dis, -1):
            res[i] += 1
        cur -= dis  # 현재 위치 갱신

# 2번 이상 지나간 영역의 크기 구하기
cnt = 0
for i in range(len(res)):
    if res[i] >= 2:
        cnt += 1

print(cnt)
# print(res[1000-55:1000])