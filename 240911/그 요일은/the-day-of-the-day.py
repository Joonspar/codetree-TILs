m1,d1,m2,d2 = map(int,input().split())
nums = [0,31,29,31,30,31,30,31,31,30,31,30,31]
date = ['Mon','Tue','Wed','Thu','Fri','Sat','Sun']
day1 = 0
A = input()
for i in range(1,m2):
    day1 += nums[i]
day1 += d2
for i in range(1,m1):
    day1 -= nums[i]
day1 -= d1
cnt = 0
print(day1//7 + 1)