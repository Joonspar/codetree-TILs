a = input()
li = []
for ele in a[1::2]:
    li.append(ele)
print(*li[::-1],sep='')