n=int(input())
arr=list(input().split())
arr.sort()
for i in range(n):
    lgth=len(arr)
    if (i+1)%2==1:
        # 중앙값 인덱스 = (lgth+1)/2 -1
        mid = int((lgth+1)/2 -1)
        print(arr[mid],end=" ")