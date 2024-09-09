a,b = map(int,input().split())

def func1(n):
    ans = str(n)
    if '3' in ans or '6' in ans or '9' in ans:
        return True

def func2(a,b):
    cnt = 0
    for i in range(a,b+1):
        if func1(i) or i % 3 == 0:
            cnt += 1
    return cnt

print(func2(a,b))