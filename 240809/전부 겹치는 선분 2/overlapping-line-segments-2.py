n = int(input())
section = [
    list(map(int,input().split()))
    for _ in range(n)
]
possible = False
for i in range(n):
    cnt = [0] * 101
    for j in range(n):
        if i == j:
            continue
        x1,x2 = section[j]
        for k in range(x1,x2+1):
            cnt[k] += 1
    if cnt.count(n) >= 1:
        possible = True
        break

if possible:
    print('Yes')
else:
    print('No')