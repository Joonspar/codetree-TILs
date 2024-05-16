code,color,minute = input().split()
minute = int(minute)

class Bomb:
    def __init__(self,code,color,minute):
        self.code = code
        self.color = color
        self.minute = minute

sel = Bomb(code,color,minute)
print("code :",code)
print("color :",color)
print("second :",minute)