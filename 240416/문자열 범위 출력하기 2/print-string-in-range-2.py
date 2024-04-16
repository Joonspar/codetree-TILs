s = input()
n = int(input())
for i in range(len(s)-1,len(s)-n-1,-1):
    print(s[i],end='')