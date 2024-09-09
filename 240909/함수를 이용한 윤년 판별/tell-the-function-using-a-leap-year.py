y = int(input())

def check(y):
    if y % 4 == 0 or (y % 400 == 0 and y % 100 != 0):
        return 'true'
    else:
        return 'false'

print(check(y))