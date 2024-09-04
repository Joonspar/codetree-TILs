a = input()
directions = list(input())
l1 = len(a)
l2 = len(directions)
for i in range(l2):
    if directions[i] == 'L':
        a = a[1:] + a[0]
        # print(a)
    else:
        a = a[-1] + a[:l1-1]
        # print(a)
print(a)