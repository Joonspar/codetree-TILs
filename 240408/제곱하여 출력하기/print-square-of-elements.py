n = input()
li = list(map(int,input().split()))

li1 = [elem ** 2 for elem in li]
print(*li1)