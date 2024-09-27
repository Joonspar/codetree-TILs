n,k = map(int,input().split())
ans = 0
arr = [0] * 10001
for _ in range(n):
    a,b = input().split()
    arr[int(a)] = b

for i in range(10001-k):
    score = 0
    for j in range(i,i+k+1):
        if arr[j] == 'G':
            score += 1
        elif arr[j] == 'H':
            score += 2
    ans = max(score,ans)
print(ans)