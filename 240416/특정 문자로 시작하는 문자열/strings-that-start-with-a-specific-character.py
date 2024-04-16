n = int(input())
li = []
cnt = 0
res = 0
for _ in range(n):
    s = input()
    li.append(s)
c = input()

for i in li:
    if i[0] == c:
        cnt += 1
        res += len(i)
print(cnt,"%.2f" %(res/cnt))