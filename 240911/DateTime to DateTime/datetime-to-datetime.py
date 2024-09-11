a,b,c = map(int,input().split())
o_d , o_h , o_m = 11,11,11
total = 0
total += 1440*(a-o_d)
if o_m >= c:
    total += (60*(b-o_h-1) + (60-abs(o_m-c))) 
else:
    total += (60*(b-o_h) + c-o_m)
no = True
if a == 11:
    if b == 11 and c < 11:
        no = False
    elif b < 11:
        no = False

if no:
    print(total)
else:
    print(-1)