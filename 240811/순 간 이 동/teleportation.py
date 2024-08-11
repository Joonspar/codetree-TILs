A,B,x,y = map(int,input().split())
p1 = abs(B - A)
p2 = abs(x-A) + abs(B-y)
p3 = abs(y-A) + abs(B-x)

print(min(p1,p2,p3))