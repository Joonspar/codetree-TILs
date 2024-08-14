def max_product_of_three(nums):
    # 정렬
    nums.sort()
    
    # 세 개의 가장 큰 값 곱하기
    max1 = nums[-1] * nums[-2] * nums[-3]
    
    # 두 개의 가장 작은 값(음수)과 가장 큰 값 곱하기
    max2 = nums[0] * nums[1] * nums[-1]
    
    # 두 값 중 최대값 반환
    return max(max1, max2)

# 입력 받기
n = int(input())
nums = list(map(int, input().split()))

# 결과 출력
print(max_product_of_three(nums))