def min_cost_to_limit_range(n, k, nums):
    # 입력 수들을 정렬
    nums.sort()
    
    min_cost = float('inf')
    
    # 슬라이딩 윈도우로 가능한 범위를 찾기
    for i in range(n):
        for j in range(i, n):
            if nums[j] - nums[i] > k:
                break
            
            min_val = nums[i]
            max_val = nums[j]
            
            # 비용 계산
            cost = 0
            for num in nums:
                if num < min_val:
                    cost += min_val - num
                elif num > max_val:
                    cost += num - max_val
            
            min_cost = min(min_cost, cost)
    
    return min_cost

# 입력 받기
import sys
input = sys.stdin.read
data = input().split()

n = int(data[0])
k = int(data[1])
nums = list(map(int, data[2:]))

# 결과 출력
print(min_cost_to_limit_range(n, k, nums))