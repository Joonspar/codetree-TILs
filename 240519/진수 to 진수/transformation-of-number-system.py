a,b = map(int,input().split())
n = input()
s = 0
for i in range(len(n)-1,-1,-1):
    s += int(n[i]) * (a**(len(n)-i-1))
arr = []
while s>=2:
    arr.append(s%b)
    s //= b
arr.append(s)

print(*arr[::-1],sep='')