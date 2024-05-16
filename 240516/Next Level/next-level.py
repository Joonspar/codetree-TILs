ID,LEVEL = input().split()
level = int(LEVEL)
class NL:
    def __init__(self,idd='codetree',lv=10):
        self.idd = idd
        self.lv = lv
p1 = NL()
print("user {} lv {}".format(p1.idd,p1.lv))


p2 = NL(ID,level)
print("user {} lv {}".format(p2.idd,p2.lv))