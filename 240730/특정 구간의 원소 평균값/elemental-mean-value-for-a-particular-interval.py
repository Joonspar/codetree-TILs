n = int(input())
arr = list(map(int,input().split()))
cnt = 0

for k in range(1, n+1): 
    for i in range(n - k + 1):
        tgt = arr[i:i+k]
        mean = sum(tgt)/k
        if mean in tgt:
            cnt += 1

print(cnt)