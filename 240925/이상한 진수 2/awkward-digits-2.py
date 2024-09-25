import sys 
INT_MAX = sys.maxsize
INT_MIN = -sys.maxsize
ans = INT_MIN

a = list(input()) 
l = len(a) # a의 길이
for i in range(l):
    res = 0
    if a[i] == '1':
        a[i] = '0'
    else:
        a[i] = '1'
    for j in range(l):
        res += int(a[j]) * (2 ** (l-j-1))
    if a[i] == '1':
        a[i] = '0'
    else:
        a[i] = '1'
    ans = max(ans,res)
print(ans)