def find_infected_developers(N, K, P, T, handshakes):
    # Initialize the infection status and handshake count for each developer
    infected = [0] * N
    handshake_count = [0] * N
    
    # Mark the initially infected developer
    infected[P - 1] = 1
    
    # Sort the handshakes by time
    handshakes.sort()
    
    # Process each handshake in order
    for t, x, y in handshakes:
        x -= 1  # Convert to 0-index
        y -= 1  # Convert to 0-index
        
        # Increase handshake count for infected developers
        if infected[x] == 1:
            handshake_count[x] += 1
        if infected[y] == 1:
            handshake_count[y] += 1
        
        # Check infection status and infect other developer if possible
        if infected[x] == 1 and handshake_count[x] <= K:
            infected[y] = 1
        if infected[y] == 1 and handshake_count[y] <= K:
            infected[x] = 1
    
    return ''.join(map(str, infected))

# Input reading
N, K, P, T = map(int, input().split())
handshakes = []
for _ in range(T):
    t, x, y = map(int, input().split())
    handshakes.append((t, x, y))

# Find the infected developers and print the result
result = find_infected_developers(N, K, P, T, handshakes)
print(result)