month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

m1,d1,m2,d2 = map(int,input().split())
s = 0
if d1 > d2:
    for i in range(m1,m2):
        s += month[i]
    s -= (d1-d2+1)
else:
    for i in range(m1,m2):
        s += month[i]
    s += (d2-d1+1)
print(s)