class CodeName:
    def __init__(self,name,score):
        self.name = name
        self.score = score

li = []
for _ in range(5):
    name,score = tuple(map(str,input().split()))
    score = int(score)
    li.append(CodeName(name,score))

idx = 0
for j in range(1,5):
    if li[idx].score > li[j].score:
        idx = j
print(li[idx].name,li[idx].score)