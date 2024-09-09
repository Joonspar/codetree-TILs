n,m = map(int,input().split())
def gmd(n,m):
    ans = 1
    for i in range(1,min(n,m)+1):
        if n % i == 0 and m % i == 0:
            res = i
        ans = max(ans,res)
    return ans
print(gmd(n,m))