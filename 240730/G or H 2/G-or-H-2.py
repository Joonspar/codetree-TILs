# 입력 처리
N = int(input())
people = []

for _ in range(N):
    position, alpha = input().split()
    position = int(position)
    people.append((position, alpha))

# 위치를 기준으로 정렬
people.sort()

# 최대 사진 크기 계산
max_photo_size = 0

# 슬라이딩 윈도우 방식으로 가능한 최대 구간 찾기
for start in range(N):
    g_count = 0
    h_count = 0
    for end in range(start, N):
        if people[end][1] == 'G':
            g_count += 1
        else:
            h_count += 1
        
        # 조건을 만족하는 경우, 사진 크기 계산
        if g_count == h_count or g_count == 0 or h_count == 0:
            photo_size = people[end][0] - people[start][0]
            if end != start:
                max_photo_size = max(max_photo_size, photo_size)

# 결과 출력
print(max_photo_size)