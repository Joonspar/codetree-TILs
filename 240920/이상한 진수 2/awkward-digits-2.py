import sys
INT_MAX = sys.maxsize
INT_MIN = -sys.maxsize
ans = INT_MIN
a = list(input())
l = len(a)
for i in range(l):
    s = 0
    if a[i] == '1':
        a[i] = '0'
    else:
        a[i] = '1'
    for j in range(l-1,-1,-1):
        a[j] = int(a[j])
        s += (2**(l-1-j)) * a[j]
    ans = max(s,ans)
    if a[i] == 1:
        a[i] = 0
    else:
        a[i] = 1
print(ans)