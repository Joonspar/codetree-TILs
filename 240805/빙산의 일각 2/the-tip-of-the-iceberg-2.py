n = int(input())
heights = []
for _ in range(n):
    heights.append(int(input()))
ans = 0
for i in range(1,1001):
    cnt = 0
    is_chunk = True
    for j in range(n):
        if heights[j] <= i:
            is_chunk = True
        elif heights[j] > i and is_chunk == True:
            is_chunk = False
            cnt += 1
    ans = max(ans,cnt)
print(ans)