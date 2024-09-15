n = int(input())
arr = [
    list(input().split())
    for _ in range(n)
]
res = ['G'] * (n*101)
cur = (n*101) // 2
for a,b in arr:
    a = int(a)
    if b == 'R':
        for i in range(cur,cur+a):
            res[i] = 'B'
        cur += (a-1)
    
    else:
        for i in range(cur,cur-a,-1):
            res[i] = 'W'
        cur -= (a-1)

cntw , cntb = 0,0
for elem in res:
    if elem == 'B':
        cntb += 1
    elif elem == 'W':
        cntw += 1
print(cntw,cntb)