x,y = map(int,input().split())
res = []
for i in range(x,y+1):
    s = 0
    i = str(i)
    for elem in i:
        elem = int(elem)
        s += elem
    res.append(s)
print(max(res))