n = int(input())

for i in range(n):
    if i % 2 == 0:
        print('*',end='')
    else:
        print('* '*(i+1),end='')
    print()