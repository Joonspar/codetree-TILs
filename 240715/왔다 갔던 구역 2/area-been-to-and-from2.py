def count_overlapped_areas(n, commands):
    position = 0
    positions = {}

    for command in commands:
        steps, direction = command.split()
        steps = int(steps)
        
        if direction == 'R':
            for i in range(1, steps + 1):
                new_position = position + i
                if new_position in positions:
                    positions[new_position] += 1
                else:
                    positions[new_position] = 1
            position += steps
        elif direction == 'L':
            for i in range(1, steps + 1):
                new_position = position - i
                if new_position in positions:
                    positions[new_position] += 1
                else:
                    positions[new_position] = 1
            position -= steps

    overlapped_count = sum(1 for pos in positions if positions[pos] >= 2)

    return overlapped_count

# 입력 받기
n = int(input())
commands = [input().strip() for _ in range(n)]

# 결과 출력
print(count_overlapped_areas(n, commands))