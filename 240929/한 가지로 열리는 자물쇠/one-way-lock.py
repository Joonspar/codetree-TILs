n = int(input())
n1,n2,n3 = map(int,input().split())
ans = n ** 3
for i in range(1,n+1):
    for j in range(1,n+1):
        for k in range(1,n+1):
            if abs(i-n1) > 2 and abs(j-n2) > 2 and abs(k-n3) > 2:
                ans -= 1
print(ans)