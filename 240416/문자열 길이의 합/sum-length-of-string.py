n = int(input())
t = 0
cnt = 0
for _ in range(n):
    a = input()
    a = a.replace(" ","")
    t += len(a)
    if a[0] == 'a':
        cnt += 1
print(t, cnt)