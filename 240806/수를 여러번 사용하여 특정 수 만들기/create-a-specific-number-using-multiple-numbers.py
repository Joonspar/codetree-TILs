a,b,c = map(int,input().split())
ans = 0
for i in range(1000):
    if a*i > c:
        break
    for j in range(1000):
        res_a = a*i
        res_b = b*j
        if res_a + res_b > c:
            ans = max(ans,res_a+b*(j-1))
            break
print(ans)