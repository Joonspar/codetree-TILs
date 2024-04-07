a = list(map(int,input().split()))
total = 0
cnt = 0
for i in range(len(a)):
    if a[i] != 0:
        total += a[i]
        cnt += 1
    else:
        break
print(total,round((total/cnt),1))