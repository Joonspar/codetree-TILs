s = input()
l = len(s)

for i in range(l):
    if 'A' <= s[i] <= 'Z':
        print(s[i].lower(),end='')
    else:
        print(s[i].upper(),end='')