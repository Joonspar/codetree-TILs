def max_min_distance(n, seats):
    max_distance = 0

    for i in range(n):
        if seats[i] == '0':
            seats[i] = '1'
            min_distance = n

            last_person = -1
            for j in range(n):
                if seats[j] == '1':
                    if last_person != -1:
                        min_distance = min(min_distance, j - last_person)
                    last_person = j

            max_distance = max(max_distance, min_distance)
            seats[i] = '0'

    return max_distance

n = int(input())
seats = list(input().strip())

print(max_min_distance(n, seats))