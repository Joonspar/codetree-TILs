import sys
INT_MAX = sys.maxsize
INT_MIN = -sys.maxsize
ans = INT_MAX

li = list(map(int,input().split()))

def get_diff(i,j,k):
    team1 = li[i] + li[j] + li[k]
    team2 = sum(li) - team1
    return abs(team1 - team2)

for i in range(6):
    for j in range(i+1,6):
        for k in range(j+1,6):
            res = get_diff(i,j,k)
        ans = min(res,ans)
print(ans)