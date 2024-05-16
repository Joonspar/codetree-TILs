n=int(input())
arr=list(input().split())
arr2=[]

for i in range(n):
    arr2.append(arr[i])
    arr2.sort()
    lgth=len(arr2)
    if (i+1)%2==1:
        # 중앙값 인덱스 = (lgth+1)/2 -1
        mid = int((lgth+1)/2 -1)
        print(arr2[mid],end=" ")