a,b,c = map(int,input().split())
o_d , o_h , o_m = 11,11,11
total = 0
total += 1440*(a-o_d)
if o_m >= c:
    total += (60*(b-o_h-1) + (60-abs(o_m-c))) 
else:
    total += (60*(b-o_h) + c-o_m)

if a == 11 and b <= 11:
    if c < 11:
        print(-1)
else:
    print(total)