n = int(input())
arr = list(map(int,input().split()))
new_arr = sorted(arr)
ans = -1
for i in range(n-1):
    if new_arr[i] != new_arr[i+1]:
        ans = new_arr[i+1]
        break

if arr.count(ans) < 1 or arr.count(ans) >= 2:
    print(-1)
else:
    print(arr.index(ans)+1)