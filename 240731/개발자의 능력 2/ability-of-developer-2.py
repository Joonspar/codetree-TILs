arr = list(map(int,input().split()))
min_diff = 1000000
def get_diff(i,j):
    first = arr[i] + arr[j]
    second = arr[i-1] + arr[j-1]
    third = sum(arr) - first - second
    return max(first,second,third) - min(first,second,third)
for i in range(1,6):
    for j in range(1,6):
        min_diff = min(min_diff,get_diff(i,j))
print(min_diff)