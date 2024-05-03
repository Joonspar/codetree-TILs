a,b,c,d = map(int,input().split())

pre = 60*a + b
suc = 60*c + d

now = suc - pre
print(now)