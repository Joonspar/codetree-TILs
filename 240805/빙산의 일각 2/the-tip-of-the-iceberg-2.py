n = int(input())
heights = []
bulk = 0
is_seperated = False
for _ in range(n):
    heights.append(int(input()))
for i in range(1,1001):
    cnt = 0
    for j in range(n):
        heights[j] -= i
    for k in range(1,n):
        if heights[k-1] > 0 and heights[k] <= 0:
            cnt += 1
    bulk = max(bulk,cnt)
    for l in range(n):
        heights[l] += i
print(bulk+1)