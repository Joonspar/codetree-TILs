n = int(input())
arr = list(map(int, input().split()))

prev_min_idx = 0 
min_idx = 0

for i in range(prev_min_idx, n):
    if arr[i] < arr[min_idx]:
        min_idx = i

    prev_min_idx = min_idx

max_idx = min_idx
for j in range(prev_min_idx, n):
    if arr[max_idx] < arr[j]:
        max_idx = j
    
    prev_min_idx = max_idx

if min_idx == n - 1:
    print("0")
else:
    print(arr[max_idx] - arr[min_idx])