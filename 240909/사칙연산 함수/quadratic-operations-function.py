a,o,c = input().split()
def add(a,c):
    a,c = int(a),int(c)
    print(f'{a} + {c} = {a+c}')
def diff(a,c):
    a,c = int(a),int(c)
    print(f'{a} - {c} = {a-c}')
def div(a,c):
    a,c = int(a),int(c)
    print(f'{a} // {c} = {a/c}')
def mul(a,c):
    a,c = int(a),int(c)
    print(f'{a} * {c} = {a*c}')

if o == '+':
    add(a,c)
elif o == '-':
    diff(a,c)
elif o == '/':
    div(a,c)
elif o == '*':
    mul(a,c)
else:
    print('False')