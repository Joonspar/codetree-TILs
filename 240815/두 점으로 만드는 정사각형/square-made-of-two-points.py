x1,y1,x2,y2 = map(int,input().split())
a1,b1,a2,b2 = map(int,input().split())

h = max(x1,a1,x2,a2) - min(x1,x2,a1,a2)
w = max(b1,b2,y1,y2) - min(b1,b2,y1,y2)

if h > w:
    print(h**2)
else:
    print(w ** 2)