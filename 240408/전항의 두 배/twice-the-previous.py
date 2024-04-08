li = list(map(int,input().split()))

for i in range(3,11):
    li.append(2*li[-2]+li[-1])
print(*li)