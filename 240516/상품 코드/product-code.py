name,cod = input().split()

class code:
    def __init__(self,name='codetree',code='50'):
        self.name = name
        self.code = code

s1 = code()
s2 = code(name,cod)

print("product {} is {}".format(s1.code,s1.name))
print("product {} is {}".format(s2.code,s2.name))