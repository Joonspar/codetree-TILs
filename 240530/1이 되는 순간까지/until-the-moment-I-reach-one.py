n = int(input())
def fn(n,cnt):
    if n == 1:
        return cnt
    elif n % 2 == 0:
        cnt += 1
        return fn(n/2,cnt)
    else: 
        cnt += 1
        return fn(n//3,cnt)
cnt = fn(n,0)
print(cnt)