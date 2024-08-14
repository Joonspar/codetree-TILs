from collections import deque

# 1. 격자에서 특정 문자 ('L', 'R', 'B')의 위치를 찾는 함수
def find_position(grid, target):
    for i in range(10):
        for j in range(10):
            if grid[i][j] == target:
                return (i, j)

# 2. BFS를 사용해 'L'에서 'B'로 가는 최단 거리를 구하는 함수
def bfs(grid, start, target, avoid):
    queue = deque([start])  # 출발점 넣기
    visited = [[False] * 10 for _ in range(10)]  # 방문 여부를 체크하기 위한 배열
    visited[start[0]][start[1]] = True  # 시작점 방문 표시

    # 상하좌우 방향으로 움직이기 위한 방향 벡터
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    steps = 0  # 몇 칸을 이동했는지 세는 변수

    while queue:
        for _ in range(len(queue)):
            x, y = queue.popleft()
            
            # 목표 지점 'B'에 도달하면 현재까지의 이동 횟수를 반환
            if (x, y) == target:
                return steps
            
            # 네 방향으로 이동
            for dx, dy in directions:
                nx, ny = x + dx, y + dy

                # 격자 범위를 벗어나지 않고, 방문하지 않았으며, R이 아닌 칸으로 이동
                if 0 <= nx < 10 and 0 <= ny < 10 and not visited[nx][ny] and grid[nx][ny] != avoid:
                    visited[nx][ny] = True  # 방문 표시
                    queue.append((nx, ny))  # 다음 탐색을 위해 큐에 넣기
        
        steps += 1  # 한 단계 탐색이 끝날 때마다 이동 거리 증가
    
    return -1  # 목표에 도달할 수 없는 경우

# 3. 전체 코드를 실행하는 메인 함수
def main():
    grid = [input().strip() for _ in range(10)]  # 격자 입력받기

    start = find_position(grid, 'L')  # 'L'의 위치 찾기
    target = find_position(grid, 'B')  # 'B'의 위치 찾기
    
    # 'L'에서 'B'까지의 최단 거리 계산 (R을 피해야 함)
    shortest_path_length = bfs(grid, start, target, 'R')

    # 결과 출력 (출발점과 도착점을 제외한 거리이므로 1을 뺌)
    print(shortest_path_length - 1)

# 4. 메인 함수 실행
if __name__ == "__main__":
    main()