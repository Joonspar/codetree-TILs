n = int(input())
li = list(map(int,input().split()))
mi = li[0]
for i in li:
    if mi > i:
        mi = i
print(mi, li.count(mi))