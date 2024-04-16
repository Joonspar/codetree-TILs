s = input()
n = int(input())
if len(s) > n:
    for i in range(len(s)-1,len(s)-n-1,-1):
        print(s[i],end='')
else:
    print(s[::-1])