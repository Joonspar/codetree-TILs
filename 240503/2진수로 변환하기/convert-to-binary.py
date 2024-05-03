n = int(input())
arr = []

while n > 0:
    if n < 2:
        arr.append(n)
        break
    arr.append(n%2)
    n //= 2
print(*arr[::-1],sep='')