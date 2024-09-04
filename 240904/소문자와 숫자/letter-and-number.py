s = input()
ans = []
s = s.lower()

for i in range(len(s)):
    if 'a' <= s[i] <= 'z' or '0' <= s[i] <= '9':
        ans.append(s[i])
print(*ans,sep='')