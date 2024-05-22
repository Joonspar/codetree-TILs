n = int(input())
arr = list(map(int,input().split()))

res = 0
for i in range(n):
    for j in range(n-1):
        s = 0
        if j == i+1 or j == i-1:
            continue
        s = arr[j] + arr[i] 
        res = max(s,res)
res = max(s,res)
print(res)