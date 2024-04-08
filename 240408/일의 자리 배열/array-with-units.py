arr=list(map(int,input().split()))

for i in range(2,10):

    arr.append(arr[-1]+arr[-2])
    if arr[i]>=10:
        arr[i]=arr[i]%10

for i in arr:

    print(i,end=" ")