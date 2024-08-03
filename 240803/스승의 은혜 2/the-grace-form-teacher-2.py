n,b = map(int,input().split())
p = []
count = [0] * n
for _ in range(n):
    price = int(input())
    p.append(price)
p.sort()
for i in range(n):
    total = 0
    for j in range(n):
        if i == j:
            total += p[j] // 2
        else:
            total += p[j]
        if total <= b:
            count[i] += 1
        else:
            break
print(max(count))