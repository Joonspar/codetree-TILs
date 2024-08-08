n = int(input())
max_gap = 17
heights = []
for _ in range(n):
    heights.append(int(input()))
heights.sort()
cost = 10000
x = 1
while heights[-1] - heights[0] > max_gap:
    heights[-1] -= x
    heights[0] += x
    x += 1
ans = x**2 + x**2
print(ans)