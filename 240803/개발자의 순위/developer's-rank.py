k, n = map(int, input().split())
cnt = 0
result = [
    tuple(map(int, input().split()))
    for _ in range(k)
]

for a in range(n):
    for b in range(n):
        if a == b:
            continue
        win = True
        for i in range(k):
            if result[i].index(a + 1) > result[i].index(b + 1):
                win = False
                break
        if win:
            cnt += 1

print(cnt)