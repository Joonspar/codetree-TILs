def count_overlapped_areas(n, commands):
    position = 0
    positions = {}
    
    for command in commands:
        steps, direction = command.split()
        steps = int(steps)
        
        if direction == 'R':
            for _ in range(steps):
                position += 1
                if position in positions:
                    positions[position] += 1
                else:
                    positions[position] = 1
        elif direction == 'L':
            for _ in range(steps):
                position -= 1
                if position in positions:
                    positions[position] += 1
                else:
                    positions[position] = 1
    
    overlapped_count = sum(1 for pos in positions if positions[pos] >= 2)
    
    return overlapped_count

# 입력 받기
n = int(input())
commands = [input().strip() for _ in range(n)]

# 결과 출력
print(count_overlapped_areas(n, commands))