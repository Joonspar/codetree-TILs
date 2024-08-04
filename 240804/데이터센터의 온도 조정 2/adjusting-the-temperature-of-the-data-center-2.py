n,c,g,h = map(int,input().split())
t_a = []
t_b = []
for i in range(n):
    a,b = map(int,input().split())
    t_a.append(a)
    t_b.append(b)

def section(l,t,r):
    if t < l:
        return c
    elif l <= t and t <= r:
        return g
    else:
        return h

def total(t):
    res = 0
    for i in range(n):
        res += section(t_a[i],t,t_b[i])
    return res
ans = 0
for t in range(1,1001):
    ans = max(ans,total(t))
print(ans)