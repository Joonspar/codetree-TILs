s1,s2 = input().split()
l1,l2 = len(s1),len(s2)
ans = []
z = ''
for i in range(l1):
    if '0' <= s1[i] <='9':
        z += s1[i]
    else:
        ans.append(z)
        break
z= ''
for i in range(l2):
    if '0' <= s2[i] <= '9':
        z += s2[i]
    else:
        break
ans.append(z)

su = 0
for i in range(len(ans)):
    su += int(ans[i])
print(su)