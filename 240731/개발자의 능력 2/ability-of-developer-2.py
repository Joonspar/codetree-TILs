# 입력 받기
arr = list(map(int, input().split()))

# 가능한 조합의 수를 최소 차이로 계산하기
min_diff = float('inf')

def get_diff(i, j, k, l):
    first = arr[i] + arr[j]
    second = arr[k] + arr[l]
    third = sum(arr) - first - second
    return max(first, second, third) - min(first, second, third)

# 6명의 인덱스: 0, 1, 2, 3, 4, 5
for i in range(6):
    for j in range(i + 1, 6):
        for k in range(6):
            if k == i or k == j:
                continue
            for l in range(k + 1, 6):
                if l == i or l == j:
                    continue
                # 나머지 2명의 인덱스를 찾아서 세 번째 팀을 구성합니다.
                remaining = [m for m in range(6) if m not in [i, j, k, l]]
                # get_diff 함수 호출
                diff = get_diff(i, j, k, l)
                # 최소 차이 업데이트
                if diff < min_diff:
                    min_diff = diff

# 결과 출력
print(min_diff)