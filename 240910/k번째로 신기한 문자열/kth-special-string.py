n,k,T = input().split()
n,k = int(n),int(k)

def check(a,b):
    if len(a) < len(b):
        return False
    return a[:len(b)] == b

li = []

for i in range(n):
    s = input()
    if check(s,T):
        li.append(s)

li.sort()
print(li[k-1])