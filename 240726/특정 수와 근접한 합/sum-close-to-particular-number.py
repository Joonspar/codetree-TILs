def find_min_difference(N, S, numbers):
    total_sum = sum(numbers)
    target_sum = total_sum - S

    # 가능한 모든 두 수의 조합을 찾습니다.
    min_diff = float('inf')
    for i in range(N):
        for j in range(i + 1, N):
            two_sum = numbers[i] + numbers[j]
            remaining_sum = total_sum - two_sum
            current_diff = abs(remaining_sum - S)
            if current_diff < min_diff:
                min_diff = current_diff

    return min_diff

# 입력 받기
N, S = map(int, input().split())
numbers = list(map(int, input().split()))

# 결과 출력
result = find_min_difference(N, S, numbers)
print(result)