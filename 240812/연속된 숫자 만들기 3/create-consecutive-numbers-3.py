a, b, c = list(map(int, input().split()))

f_dist = abs(a-b)
s_dist = abs(b-c)

count = 0

if f_dist == 1 and s_dist == 1:
    count = 0
elif f_dist <= 2 and s_dist <= 2:
    count = 1
else:
    count = max(f_dist, s_dist) - 1

print(count)