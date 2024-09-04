s,q = input().split()
q = int(q)
l = len(s)
l2 = l // 2
for i in range(q):
    num = int(input())
    if num == 1:
        s = s[1:] + s[0]
        print(s)
    elif num == 2:
        s = s[-1] + s[0:len(s)-1]
        print(s)
    elif num == 3:
        s = s[::-1]
        print(s)