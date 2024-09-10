secret , place , time = input().split()
time = int(time)
class a007:
    def __init__(self,se,pl,ti):
        self.s = se
        self.p = pl
        self.t = ti

mission = a007(secret,place,time)
print(f'secret code : {mission.s}')
print(f'meeting point : {mission.p}')
print(f'time : {mission.t}')