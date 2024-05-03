days = [0,31,20,31,30,31,30,31,31,30,31,30,31]

def gdays(month,day):
    result = 0
    for i in range(1,month):
        result += days[i]
    result += day

    return result

m1,d1,m2,d2 = map(int,input().split())

print(gdays(m2,d2) - gdays(m1,d1) + 1)