arr = [
    list(map(int,input().split()))
    for _ in range(2)
]
for i in range(2):
    sum1 = 0
    for j in range(4):
        sum1 += arr[i][j] 
    print(round(sum1/4,1),end=' ')
print()

for i in range(4):
    sum2 = 0
    for j in range(2):
        sum2 += arr[j][i]
    print(round(sum2/2,1),end=' ')
print()
sum3 = 0
for i in range(2):
    sum3 += sum(arr[i])
print(round(sum3/8,1))