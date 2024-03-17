from collections import deque

R, C = map(int, input().split())
cave = [] # 동굴 모양
for r in range(R):
    cave.append(list(map(str, input())))
N = int(input()) # 던진 횟수
H = list(map(int, input().split())) # 던진 높이

# 던지고, 파괴된다
def throw(cave, index):
    h = H[index] - 1
    if index % 2 == 0:  # 창영 turn (좌축 > 우측)
        for c in range(C):
            if cave[R - h][c] == 'x':
                cave[R - h][c] = '.'
                break
    else:               # 상근 turn (우측 > 좌측)
        for c in range(C - 1, -1):
            if cave[R - h][c] == 'x':
                cave[R - h][c] = '.'
                break
    return cave

# 클러스터가 분리됐는지 탐색
def check_cluster(cave):
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    que = deque()
    visited = [[False for _ in range(C)] for _ in range(R)]
    for r in range(R):
        for c in range(C):
            if cave[r][c] == 'x':
                que.append((r,c))
                break
    cluster = []
    while que:
        x, y = que.popleft()
        if not visited[x][y]:
            visited[x][y] = True
            cluster.append((x, y))
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= R or ny < 0 or ny >= C:
                continue
            if cave[nx][ny] == 'x' and not visited[nx][ny]:
                que.append((nx, ny))
    if len(cluster) == 0:
        check = False
    else:
        check = True

    return check, cluster, visited


# 분리된 클러스터 바닥으로 이동
def move_cluster(cave, cluster, visited):
    down_min = 1e9
    for x, y in cluster:
        down_cnt = 0
        for r in (x + 1, R):
            if cave[r][y] == '.':
                down_cnt += 1
            elif cave[r][y] == 'x' and not visited[r][y]:
                break
        down_min = min(down_min, down_cnt)
    for x, y in cluster:
        cave[x][y] = '.'
        cave[x + down_min][y] = 'x'

    return cave



for turn in range(N):
    cave = throw(cave, turn)
    check, cluster, visited = check_cluster(cave)
    if check:
        cave = move_cluster(cave, cluster, visited)

print(cave)