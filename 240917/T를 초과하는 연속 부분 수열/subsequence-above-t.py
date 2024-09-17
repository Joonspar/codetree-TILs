n,t = map(int,input().split())
arr = list(map(int,input().split()))

res = 1
cnt = 1
for i in range(1,n):
    if arr[i-1] > t and arr[i] > t:
        cnt += 1
    else:
        res = max(cnt,res)
        cnt = 1
    res = max(cnt,res)
print(res)