n = int(input())
arr = [
    int(input())
    for _ in range(n)
]

cnt = 1
res = 1
for i in range(1,n):
    if arr[i-1] < arr[i]:
        cnt += 1
    else:
        res = max(cnt,res)
        cnt = 1
    res = max(cnt,res)
print(res)