n,k,t = input().split()
n,k = int(n),int(k)
li = []
li2 = []
for i in range(n):
    li.append(input())
for i in range(n):
    if li[i][:len(t):] == t:
        li2.append(li[i])
li2.sort()
print(li2[k-1])

# n,k,T=input().split()