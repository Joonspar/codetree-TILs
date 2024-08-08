def is_possible(mid, numbers, n, m):
    count = 1
    current_sum = 0
    
    for num in numbers:
        if current_sum + num > mid:
            count += 1
            current_sum = num
            if count > m:
                return False
        else:
            current_sum += num
    
    return True

def minimize_max_partition_sum(n, m, numbers):
    left, right = max(numbers), sum(numbers)
    result = right
    
    while left <= right:
        mid = (left + right) // 2
        if is_possible(mid, numbers, n, m):
            result = mid
            right = mid - 1
        else:
            left = mid + 1
    
    return result

# 입력 받기
n, m = map(int, input().split())
numbers = list(map(int, input().split()))

# 결과 출력
print(minimize_max_partition_sum(n, m, numbers))