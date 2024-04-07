n1 = list(map(int,input().split()))
t1 = 0
t2 = 0

for i in range(0,10,2):
    t1 += n1[i]
for i in range(1,10,2):
    t2 += n1[i]

print(abs(t1-t2))