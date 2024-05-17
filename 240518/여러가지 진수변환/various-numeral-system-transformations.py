n,b = map(int,input().split())

if b == 4:
    li = []
    while n>4:
        li.append(n%b)
        n //= b
    li.append(n)
    print(*li[::-1],sep='')

if b == 8:
    li = []
    while n>8:
        li.append(n%b)
        n //= b
    li.append(n)
    print(*li[::-1],sep='')