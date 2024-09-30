import sys
ans = sys.maxsize
arr = list(map(int,input().split()))

def diff(i,j,k,l):
    sum1 = arr[i] + arr[j]
    sum2 = arr[k] + arr[l]
    sum3 = sum(arr) - sum1 - sum2
    ret = abs(sum1 - sum2)
    ret = max(ret, abs(sum2 - sum3))
    ret = max(ret, abs(sum3 - sum1))
    
    return ret

for i in range(6):
    for j in range(i+1,6):
        for k in range(6):
            for l in range(k+1,6):
                if k == i or k == j or l == i or l == j:
                    continue
                res = diff(i,j,k,l)
                ans = min(res,ans)
print(ans)