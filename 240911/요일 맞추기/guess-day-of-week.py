m1,d1,m2,d2 = map(int,input().split())

nums = [0,31,28,31,30,31,30,31,31,30,31,30,31]
date = ['Mon','Tue','Wed','Thu','Fri','Sat','Sun']

day1 = 0
for i in range(1,m2):
    day1 += nums[i]
day1 += d2
for i in range(1,m1):
    day1 -= nums[i]
day1 -= d1
if day1 >= 0:
    res = day1 % 7
    print(date[res])
else:
    res = day1 % 7
    print(date[res])