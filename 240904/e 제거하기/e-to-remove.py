s = list(input())

for i in range(len(s)):
    if s[i] == 'e':
        del s[i]
        break
print(*s,sep='')