n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))
cnt = 1
res = 1
for i in range(1,n):
    if arr[i-1] < arr[i]:
        cnt += 1
    else:
        cnt = 1
        res = max(res,cnt)
    res = max(res,cnt)
print(res)