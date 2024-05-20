n = int(input())
arr = []

for _ in range(n):
    arr.append(int(input()))
cnt = 1
res = 1
for i in range(1,n):
    if arr[i] < 0 and arr[i-1] < 0:
        cnt += 1
    elif arr[i] > 0 and arr[i-1] > 0:
        cnt += 1
    else:
        res = max(cnt,res) 
        cnt = 1
    res = max(cnt,res)
print(res)