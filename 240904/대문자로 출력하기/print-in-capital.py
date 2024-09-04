s = input()
ans = []
l = len(s)
s = s.upper()
for i in range(l):
    if 'A' <= s[i] <= 'Z':
        ans.append(s[i])
print(*ans,sep='')