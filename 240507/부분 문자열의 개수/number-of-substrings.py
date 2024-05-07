a = input()
b = input()
cnt = 0
for i in range(len(a)-len(b)+1):
    if b in a[i:len(b)+i:]:
        cnt += 1
print(cnt)