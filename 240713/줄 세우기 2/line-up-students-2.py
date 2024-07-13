# 키를 기준으로 오름차순
# 키가 동일하다면 몸무게 기준으로 내림차순

class Student:
    def __init__(self,height,weight,num):
        self.height = height
        self.weight = weight
        self.num = num
n = int(input())
arr = []
for i in range(n):
    height,weight = list(map(int,input().split()))
    arr.append(Student(height,weight,i+1))

arr.sort(key = lambda x: (x.height,-x.weight))

for elem in arr:
    print(elem.height, elem.weight, elem.num)