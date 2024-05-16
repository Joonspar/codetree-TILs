class CodeName:
    def __init__(self,name,score):
        self.name = name
        self.score = score

li = []
for _ in range(5):
    name,score = tuple(map(str,input().split()))
    score = int(score)
    li.append(CodeName(name,score))

small = li[0]

print(small.name,small.score)