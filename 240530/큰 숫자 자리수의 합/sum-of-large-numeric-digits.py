n1,n2,n3 = map(int,input().split())

res = str(n1*n2*n3)
li = list(res)
for i in range(len(li)):
    li[i] = int(li[i])
print(sum(li))