s = input()
t = input()
for i in range(len(s)-len(t)+1):
    if t in s[i:len(t)+i:]:
        print(i)
        break
if t not in s:
    print(-1)