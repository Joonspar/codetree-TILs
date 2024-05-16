a,b,c = input().split()
c = int(c)

class gonggongchill:
    def __init__(self,code,place,time):
        self.code = code
        self.place = place
        self.time = time

s1 = gonggongchill(a,b,c)
print('secret code :',s1.code)
print('meeting point :',s1.place)
print('time :',s1.time)