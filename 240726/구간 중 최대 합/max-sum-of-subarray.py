n,k = map(int,input().split())
max_value = 0
arr = list(map(int,input().split()))
for i in range(n-k+1):
    s = 0
    for j in range(i,i+k):
        s += arr[j]
    max_value = max(max_value,s)

print(max_value)