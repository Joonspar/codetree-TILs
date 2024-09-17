n = int(input())
arr = [
    int(input())
    for _ in range(n)
]
cnt = 1
res = 1
for i in range(1,n): 
    if arr[i] < 0 and arr[i-1] < 0:
        cnt += 1
    elif arr[i] > 0 and arr[i-1] > 0:
        cnt += 1
    else:
        res = max(res,cnt)
        cnt = 1
    res = max(res,cnt)
print(res)