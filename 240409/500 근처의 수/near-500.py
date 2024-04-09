li = list(map(int,input().split()))
li1 = []
li2 = []
for i in li:
    if i > 500:
        li1.append(i)
    else:
        li2.append(i)
print(max(li2),min(li1))