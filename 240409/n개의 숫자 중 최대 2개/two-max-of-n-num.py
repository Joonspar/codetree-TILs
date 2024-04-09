n = int(input())
li = list(map(int,input().split()))

li.sort(reverse=True)
print(li[0],li[1])