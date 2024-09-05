s1 = list(input())
s2 = list(input())
ans1 = ''
ans2 = ''
nums = ['0','1','2','3','4','5','6','7','8','9']
l1 = len(s1)
l2 = len(s2)
for i in range(l1-1,-1,-1):
    if s1[i] not in nums:
        del s1[i]

for i in range(l2-1,-1,-1):
    if s2[i] not in nums:
        del s2[i]
for elem in s1:
    ans1 += elem
for elem in s2:
    ans2 += elem
print(int(ans1) + int(ans2))