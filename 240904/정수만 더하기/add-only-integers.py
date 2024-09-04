s = input()
su = 0

for i in range(len(s)):
    if '1' <= s[i] <= '9':
        su += int(s[i])
print(su)