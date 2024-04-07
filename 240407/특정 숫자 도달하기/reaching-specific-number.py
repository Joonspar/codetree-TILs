arr = list(map(int,input().split()))
li = []
for i in range(len(arr)):
    if arr[i] < 250:
        li.append(arr[i])
    else:
        break

print(sum(li),round(sum(li)/len(li),1))