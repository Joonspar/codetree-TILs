n,k = map(int,input().split())
nums = []
new_nums = []
correct = False
for _ in range(n):
    nums.append(int(input()))
for i in range(n):
    for j in range(i+1,n):
        if j - i <= k:
            correct = True
        else:
            correct = False
            break
    if correct:
        new_nums.append(nums[i])
print(len(new_nums))