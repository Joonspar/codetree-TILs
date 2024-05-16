n = int(input())

name1,addr1,pla1 = input().split()
name2,addr2,pla2 = input().split()
name3,addr3,pla3 = input().split()

class State:
    def __init__(self,name,address,place):
        self.name = name
        self.address = address
        self.place = place

s1 = State(name3,addr3,pla3)

print('name',name3)
print('addr',addr3)
print('city',pla3)