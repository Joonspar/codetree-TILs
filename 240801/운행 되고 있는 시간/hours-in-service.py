n = int(input())

time = [
    tuple(map(int,input().split()))
    for _ in range(n)
]

m_times = 0
for i in range(n):
    counts = [0] * 1001
    for j in range(n):
        if i == j:
            continue
        start,end = time[j]
        for k in range(start,end):
            counts[k] += 1

        total = [x for x in counts if x >= 1]
    m_times = max(m_times,len(total))

print(m_times)