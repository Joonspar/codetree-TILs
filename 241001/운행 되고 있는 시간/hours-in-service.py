ans = 0
n = int(input())
time = [
    list(map(int,input().split()))
    for _ in range(n)
]
for i in range(n):
    times = [0] * 1001
    for j in range(n):
        if i == j:
            continue
        a,b = time[j]
        for k in range(a,b):
            times[k] = 1
    cnt = sum(1 for time in times if time >= 1)
    ans = max(cnt,ans)
print(ans)