n,k,T = input().split()
n,k = int(n),int(k)
li = []
for _ in range(n):
    s = input()
    same = False
    for j in range(len(T)):
        if s[j] == T[j]:
            same = True
        else:
            break
    if same:
        li.append(s)
li.sort()
print(li[k])