def find_infected_developers(N, K, P, T, handshakes):
    infected = [0] * N
    # handshake_count = [0] * N
    cnt = 0
    infected[P - 1] = 1
    handshakes.sort() # 시간순으로 정렬
    
    for t, x, y in handshakes: # index를 0으로 시작하기 위함
        x -= 1
        y -= 1
        
        if infected[x] == 1:
            if infected[y] == 0:
                infected[y] = 1
                cnt += 1
                if cnt > K:
                    break
                # handshake_count[x] += 1
        if infected[y] == 1:
            if infected[x] == 0:
                infected[x] = 1
                cnt += 1
                if cnt > K:
                    break
                # handshake_count[y] += 1
    
    return ''.join(map(str, infected))

N, K, P, T = map(int, input().split())
handshakes = [tuple(map(int, input().split())) for _ in range(T)] # handshakes에 저장
result = find_infected_developers(N, K, P, T, handshakes)
print(result)