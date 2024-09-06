m , d = tuple(map(int,input().split()))

def last(m):
    if m == 2:
        return 28
    if m == 4 or m == 6 or m == 9 or m == 11:
        return 30
    return 31

def judge_day(m,d):
    if m <= 12 and d<= last(m):
        return True
    return False

if judge_day(m,d):
    print('Yes')
else:
    print('No')