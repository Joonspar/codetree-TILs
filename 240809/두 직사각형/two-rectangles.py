x1,y1,x2,y2 = map(int,input().split())
a1,b1,a2,b2 = map(int,input().split())
if (x1 <= a1 and a1 <= x2) or (x1>=a1 and x1 <= a2) or ((y1 >= b1 and y1 <= b2) and x2 > a1) or ((b1>=y1 and b1 <= y2) and x2 > a1):
    print('overlapping')
else:
    print('nonoverlapping')