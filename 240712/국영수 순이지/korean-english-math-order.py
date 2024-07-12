class Students:
    def __init__(self,name,kor,eng,math):
        self.name = name
        self.kor = int(kor)
        self.eng = int(eng)
        self.math = int(math)

n = int(input())
arr = [list(input().split()) for _ in range(n)]
students = [Students(name, kor, eng, math) for name, kor, eng, math in arr]

students.sort(key = lambda x: (-x.kor,-x.eng,-x.math))

for elem in students:
    print(elem.name, elem.kor, elem.eng, elem.math)