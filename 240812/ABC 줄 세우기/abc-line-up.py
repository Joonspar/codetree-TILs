def minimum_swaps_to_sort(n, arr):
    swaps = 0
    # 버블 정렬을 수행하며 swap 횟수를 센다
    for i in range(n):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                # 두 요소를 교환한다
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swaps += 1
    return swaps

# 입력 받기
n = int(input())
arr = input().split()

# 최소 swap 횟수 계산
result = minimum_swaps_to_sort(n, arr)

# 결과 출력
print(result)