n = int(input())
arr = list(map(int,input().split()))
ans = 100
for i in range(n):
    arr[i] *= 2
    for j in range(n):
        remaining = []
        s = 0
        for k in range(n):
            if k != j:
                remaining.append(arr[k])
        for k in range(n-2):
            s += abs(remaining[k+1] - remaining[k])
        ans = min(s,ans)

    arr[i] //= 2

print(ans)