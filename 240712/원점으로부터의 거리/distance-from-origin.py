class Class:
    def __init__(self,x,y,num):
        self.x = x
        self.y = y
        self.num = num

n = int(input())
distances = []

for i in range(n):
    x,y = list(map(int,input().split()))
    distances.append(Class(x,y,i+1))

distances.sort(key = lambda x : (x.x + x.y),x.num)

for elem in distances:
    print(elem.num)