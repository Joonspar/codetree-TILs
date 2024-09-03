s,q = map(str,input().split())
q = int(q)
s = list(s)
for i in range(q):
    a,b,c = map(str,input().split())
    if a == '1':
        b , c = int(b) , int(c)
        temp = s[b-1]
        s[b-1] = s[c-1]
        s[c-1] = temp
        print(*s,sep='')
    else:
        for i in range(len(s)):
            if s[i] == b:
                s[i] = c
        print(*s,sep='')