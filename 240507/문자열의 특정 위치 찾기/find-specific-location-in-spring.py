s,c = map(str,input().split())

for i in range(len(s)):
    if s[i] == c:
        print(i)
        break
if c not in s:
    print('No')