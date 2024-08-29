n,m = map(int,input().split())

arr = [
    list(map(int,input().split()))
    for _ in range(n)
]
ans = 0

for i in range(n):
    cnt = 1    
    for j in range(1,n):
        if arr[i][j-1] == arr[i][j]:
            cnt += 1
        else:
            cnt = 1
        if cnt >= m:
            ans += 1
            break
    for k in range(1,n):
        if arr[k-1][i] == arr[k][i]:
            cnt += 1
        else:
            cnt = 1
        if cnt >= m:
            ans += 1
            break

if n == 1:
    print(2)
else:
    print(ans)