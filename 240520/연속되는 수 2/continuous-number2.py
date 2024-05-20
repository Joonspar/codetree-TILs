n = int(input())
cnt = 0
res = 0
arr = []

for _ in range(n):
    a = int(input())
    arr.append(a)

for i in range(1,n):
    if arr[i] == arr[i-1]:
        cnt += 1
    else:
        res = max(cnt,res)
        cnt = 0
    res = max(res,cnt)
print(res+1)