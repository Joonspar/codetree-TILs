n = int(input())

def check(n):
    s = str(n)
    res = 0
    for ele in s:
        ele = int(ele)
        res += ele
    if n % 2 == 0 and res % 5 == 0:
        return 'Yes'
    else:
        return 'No' 

print(check(n))