nums = list(map(int,input().split()))
cnt = 0 
while True:
    n1 = abs(nums[0] - nums[1])
    n2 = abs(nums[1] - nums[2])
    if n1 == n2 == 1:
        break
    if n1 == 2 or n2 == 2:
        cnt += 1
        break
    elif n1 > 2 and n2 > 2:
        if n1 > n2:
            nums[0] , nums[1] = nums[1] , nums[1] + 2
        else:
            nums[1] , nums[2] = nums[0] + 2, nums[1]
    elif abs(nums[1] - nums[2]) > 2:
        nums[0] , nums[1] = nums[1] , nums[1] + 2
    elif abs(nums[0] - nums[1]) > 2:
        nums[1],nums[2] = nums[0]+2,nums[1]
    cnt += 1

print(cnt)