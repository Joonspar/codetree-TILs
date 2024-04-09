n = int(input())
arr = list(map(int, input().split()))

# 초기 최댓값과 그 위치 설정
max_value = max(arr)
max_index = arr.index(max_value) + 1

# 초기 최댓값의 위치 출력
print(max_index, end=' ')

# 주어진 조건에 따라 최댓값의 위치들을 출력
while max_index > 1:
    max_value = max(arr[:max_index - 1]) # 현재 최댓값 이전 부분에서 최댓값을 찾음
    max_index = arr.index(max_value) + 1 # 새로운 최댓값의 위치
    print(max_index, end=' ')