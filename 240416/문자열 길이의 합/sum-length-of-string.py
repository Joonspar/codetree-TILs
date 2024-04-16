n = int(input())
li = []
t = 0
cnt = 0
for _ in range(n):
    a = input()
    a = a.replace(" ","")
    t += len(a)
    cnt += a.count('a')
print(t, cnt)