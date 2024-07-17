def find_infected_developers(N, K, P, T, handshakes):
    infected = [0] * N
    handshake_count = [0] * N
    
    infected[P - 1] = 1
    handshakes.sort()
    
    for t, x, y in handshakes:
        x -= 1
        y -= 1
        
        if infected[x] == 1 and handshake_count[x] <= K:
            infected[y] = 1
            handshake_count[x] += 1
        if infected[y] == 1 and handshake_count[y] <= K:
            infected[x] = 1
            handshake_count[y] += 1
    
    return ''.join(map(str, infected))

N, K, P, T = map(int, input().split())
handshakes = [tuple(map(int, input().split())) for _ in range(T)]
result = find_infected_developers(N, K, P, T, handshakes)
print(result)