n = int(input())
s = 0
for _ in range(n):
    n1 = int(input())
    s += n1
s = str(s)
l = len(s)
s = s[1:] + s[0]
print(s)