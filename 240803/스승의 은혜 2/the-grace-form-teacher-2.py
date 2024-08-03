n,b = map(int,input().split())
cnt = 0
p = []
count = [0] * n
for _ in range(n):
    price = int(input())
    p.append(price)

for i in range(n):
    total = 0
    cnt = 0
    for j in range(n):
        if i == j:
            p[i] = p[i] // 2
        total += p[j]
        if total <= b:
            count[i] += 1
        else:
            p[i] *= 2
            break
print(max(count))