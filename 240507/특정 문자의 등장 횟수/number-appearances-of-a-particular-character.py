s = input()
cnt1 = 0
cnt2 = 0


for i in range(len(s)-1):
    if 'ee' in s[i]+s[i+1]:
        cnt1 += 1
    if 'eb' in s[i]+s[i+1]:
        cnt2 += 1
print(cnt1,cnt2)