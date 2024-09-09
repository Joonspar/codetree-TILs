m,d = map(int,input().split())

def check(m,d):
    if m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10 or m == 12:
        if 1 <= d <= 31:
            return 'Yes'
        else:
            return 'No'
    elif m == 4 or m == 6 or m == 9 or m == 11:
        if 1 <= d <= 30:
            return 'Yes'
        else:
            return 'No'
    elif m == 2:
        if 1 <= d <= 28:
            return 'Yes'
        else:
            return 'No'
    else:
        return 'No'
print(check(m,d))