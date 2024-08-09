n = int(input())
cnt = [0] * 100
for _ in range(n):
    a,b = map(int,input().split())
    for i in range(a,b+1):
        cnt[i] += 1

if cnt.count(3) >= 1:
    print('Yes')
else:
    print('No')