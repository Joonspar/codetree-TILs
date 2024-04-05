n = int(input())
a = 65
for i in range(n):
    for j in range(i):
      print(' ',end=' ')
    for j in range(n-i,0,-1):
        print(chr(a),end=' ')
        a+=1
    print()