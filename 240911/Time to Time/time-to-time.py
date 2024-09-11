a,b,c,d = map(int,input().split())

if d >= b:
    print(60*(c-a) + d-b)

else:
    print(60*(c-a-1) + 60-abs(d-b))