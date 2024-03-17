from collections import deque
import sys
input = sys.stdin.readline

R, C = map(int, input().split())
lake = []
day = 0
for r in range(R):
    lake.append(list(map(str, input())))

start, end = None, None
for r in range(R):
    for c in range(C):
        if lake[r][c] == 'L':
            if start is None:
                start = [r, c]
            else:
                end = [r, c]
                break
    if end is not None:
        break

def melt(lake, R, C):
    water_queue = deque([(r, c) for r in range(R) for c in range(C) if lake[r][c] == '.'])

    while water_queue:
        new_water_queue = deque()  # 다음 날 처리할 물의 위치
        while water_queue:
            r, c = water_queue.popleft()

            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < R and 0 <= nc < C and lake[nr][nc] == 'X':
                    lake[nr][nc] = '.'  # 빙판을 물로 변환
                    new_water_queue.append((nr, nc))  # 새로운 물 위치 추가

        water_queue = new_water_queue  # 다음 날 처리할 물의 위치를 업데이트
    return lake

def is_connected(lake):
    que = deque()
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    visited = [[False for _ in range(C)] for _ in range(R)]
    que.append((start[0], start[1]))

    while que:
        x, y = que.popleft()
        visited[x][y] = True
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx == end[0] and ny == end[1]:
                return True
            if nx < 0 or nx >= R or ny < 0 or ny >= C or lake[nx][ny] == 'X':
                continue
            if lake[nx][ny] != 'X' and not visited[nx][ny]:
                que.append((nx, ny))

    return False

while not is_connected(lake):
    day += 1
    lake = melt(lake, R, C)
print(day)