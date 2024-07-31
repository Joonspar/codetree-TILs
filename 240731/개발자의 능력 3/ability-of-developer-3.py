arr = list(map(int,input().split()))
def get_diff(i,j,k):
    first_team = arr[i] + arr[j] + arr[k]
    second_team = sum(arr) - first_team
    return abs(first_team - second_team)

min_diff = 100
for i in range(0,6):
    for j in range(i+1,6):
        for k in range(j+1,6):
            min_diff = min(min_diff,get_diff(i,j,k))
print(min_diff)