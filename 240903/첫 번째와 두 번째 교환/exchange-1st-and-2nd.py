s = list(input())
for i in range(len(s)):
	if s[i] == 'c':
		s[i] = 'o'
		i += 1
	elif s[i] == 'o':
		s[i] = 'c'
print(*s,sep='')