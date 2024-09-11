m1,d1,m2,d2 = map(int,input().split())

nums = [0,31,28,31,30,31,30,31,31,30,31,30,31]
days = 0
for i in range(1,m2):
    days += nums[i]
days += d2

for i in range(1,m1):
    days -= nums[i]
days -= d1

print(days+1)