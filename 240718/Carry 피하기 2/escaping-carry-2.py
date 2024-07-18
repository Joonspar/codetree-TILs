n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))

max_num = -1

def check_no_carry(a, b, c):
    str_a, str_b, str_c = str(a), str(b), str(c)
    max_len = max(len(str_a), len(str_b), len(str_c))
    
    str_a = str_a.zfill(max_len)
    str_b = str_b.zfill(max_len)
    str_c = str_c.zfill(max_len)
    
    for i in range(max_len):
        if int(str_a[i]) + int(str_b[i]) + int(str_c[i]) >= 10:
            return False
    return True

for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            su = arr[i] + arr[j] + arr[k]
            if check_no_carry(arr[i], arr[j], arr[k]):
                max_num = max(max_num, su)
            
print(max_num)