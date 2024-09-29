import sys
ans = sys.maxsize
nums = list(map(int,input().split()))

def diff(i,j,k):
    sum1 = nums[i] + nums[j] + nums[k]
    sum2 = sum(nums) - sum1
    return abs(sum1-sum2)

for i in range(6):
    for j in range(i+1,6):
        for k in range(j+1,6):
            res = diff(i,j,k)
            ans = min(ans,res)
print(ans)