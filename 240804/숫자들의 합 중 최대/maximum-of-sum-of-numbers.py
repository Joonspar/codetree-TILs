x,y = map(int,input().split())
res = []
for i in range(x,y+1):
    s = 0
    d1,d2 = map(int,list(str(i)))
    s = d1 + d2
    res.append(s)
print(max(res))