li = list(input())
while True:
    if len(li) == 0:
        break
    le = int(input())
    if le < len(li):
        del li[le]
    else:
        del li[-1]
    print(*li,sep='')