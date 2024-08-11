def min_time_to_reach(X):
    time = 0  # 걸린 시간
    distance = 0  # 이동한 거리
    speed = 1  # 현재 속도

    while True:
        # 현재 속도로 이동하고 시간 증가
        distance += speed
        time += 1

        # 거리 체크
        if distance >= X and speed == 1:
            break
        
        # 다음 스텝에서 속도를 줄여야 한다면 줄이고, 아니라면 증가
        if distance + speed + 1 <= X:
            speed += 1
        else:
            speed -= 1
    
    return time

# 입력 받기
X = int(input())
# 결과 출력
print(min_time_to_reach(X)-1)