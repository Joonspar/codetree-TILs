n = int(input())
li = list(map(int,input().split()))
max = 0
l = []

for i in range(n):
    if li[i] in l:
        continue
    if li[i] in li[i+1:]:
        l.append(li[i])
        continue
    if li[i] > max:
        max = li[i]
if max_val == 0:
    print(-1)
else:
    print(max_val)