arr1=[
    list(map(int,input().split()))
    for _ in range(3)
]
input()
arr2=[
    list(map(int,input().split()))
    for _ in range(3)
]
for i in range(3):
    for j in range(3):
        to = arr2[i][j] * arr1[i][j]
        print(to,end=' ')
    print()