def minimum_wifi(n, m, people):
    count = 0
    i = 0

    while i < n:
        # 현재 위치에서 와이파이를 설치할 수 있는 가장 멀리 위치
        if people[i] == 1:
            count += 1
            # 와이파이를 설치하고 그 범위만큼 건너뛰기
            i += 2 * m + 1
        else:
            i += 1

    return count

# 입력
n, m = map(int, input().split())
people = list(map(int, input().split()))

# 최소 와이파이 개수 출력
print(minimum_wifi(n, m, people))