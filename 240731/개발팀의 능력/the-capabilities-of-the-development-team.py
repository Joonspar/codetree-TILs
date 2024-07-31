arr = list(map(int,input().split()))
min_diff = 1000
def get_diff(i,j,k):
    first = arr[i] + arr[j]
    second = arr[k]
    third = sum(arr) - first - second
    return max(first,second,third) - min(first,second,third)

for i in range(5):
    for j in range(i+1,5):
        for k in range(j+1,5):
            min_diff = min(min_diff,get_diff(i,j,k))
print(min_diff)