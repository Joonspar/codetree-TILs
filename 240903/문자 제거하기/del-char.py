li = list(input())
while len(li) > 0:
    try:
        le = int(input())
        if le < len(li):
            del li[le]
        else:
            del li[-1]
        print(*li, sep='')
    except EOFError:
        break  # EOFError 발생 시 루프를 종료