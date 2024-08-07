n = int(input())
num = [
    tuple(map(int,input().split()))
    for _ in range(n)
]
correct = False
ans = 10000
for x in range(1,ans+1):
    for a,b in num:
        x *= 2
        if a <= x <= b:
            correct = True
        else:
            correct = False
            break
    if correct:
        x //= (2**n)
        ans = min(x,ans)
print(ans)