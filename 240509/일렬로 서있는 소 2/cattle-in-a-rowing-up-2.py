n = int(input())
cnt = 0
cow = list(map(int,input().split()))
for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            if (cow[i] <= cow[j]) and (cow[j] <= cow[k]):
                cnt += 1
print(cnt)