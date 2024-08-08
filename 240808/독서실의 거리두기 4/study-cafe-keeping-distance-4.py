def max_min_distance(N, seats):
    # 빈 좌석의 인덱스를 찾습니다.
    empty_indices = [i for i, seat in enumerate(seats) if seat == '0']
    
    max_min_dist = 0
    
    # 두 개의 빈 좌석에 사람을 배치하는 모든 경우를 시도합니다.
    for i in range(len(empty_indices)):
        for j in range(i + 1, len(empty_indices)):
            # 새 배열을 만들어 사람을 배치합니다.
            new_seats = list(seats)
            new_seats[empty_indices[i]] = '1'
            new_seats[empty_indices[j]] = '1'
            
            # 최소 거리를 계산합니다.
            min_dist = N  # 최대 거리로 초기화
            last_person = -1
            for k in range(N):
                if new_seats[k] == '1':
                    if last_person != -1:
                        min_dist = min(min_dist, k - last_person)
                    last_person = k
            
            # 가능한 최대 최소 거리를 갱신합니다.
            max_min_dist = max(max_min_dist, min_dist)
    
    return max_min_dist

# 입력 받기
N = int(input())
seats = input().strip()

# 결과 출력
print(max_min_distance(N, seats))