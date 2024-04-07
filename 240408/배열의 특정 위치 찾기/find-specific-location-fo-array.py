li = list(map(int,input().split()))
total1 = 0
total2 = 0
cnt = 0
for i in range(1,10,2):
    total1 += li[i]
for i in range(2,10,3):
    total2 += li[i]
    cnt += 1
print(total1, round(total2/cnt,1))