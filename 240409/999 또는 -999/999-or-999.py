li = list(map(int,input().split()))
ma = 0
mi = li[0]
for i in li:
    if i == 999 or i == - 999:
        break
    elif ma > i:
        ma = i
    elif mi < i:
        mi = i
print(ma,mi)