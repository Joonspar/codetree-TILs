n,t = map(int,input().split())

arr = list(map(int,input().split()))
cnt = 1
res = 0
for i in range(1,n):
    if arr[i] > t and arr[i-1] > t:
        cnt += 1
    else:
        cnt = 1
        res = max(res,cnt)
    res = max(cnt,res)
print(res)