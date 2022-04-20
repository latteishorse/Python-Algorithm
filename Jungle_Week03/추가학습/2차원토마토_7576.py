# 토마토
# 7576

# 인접한 토마토는 익게됨
# 상자 크기 m,n

# 1 - 익은 토마토
# 0 - 안익은 토마토
# -1 안들어있는 칸

# 모두 익을 때까지 날짜

# bfs ------------
from collections import deque

m, n = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]
queue = deque([])
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

ans = 0

def maketomatoma(n,m):
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 1:
                queue.append([i, j])

maketomatoma(n,m)

def tomatoma():
    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = dx[i] + x
            ny =  dy[i] + y

            if 0 <= nx < n and 0 <= ny < m and matrix[nx][ny] == 0:
                matrix[nx][ny] = matrix[x][y] + 1
                queue.append([nx, ny])

tomatoma()

for i in matrix:
    for j in i:
        if j == 0:
            print(-1)
            exit()
    ans = max(ans, max(i))
print(ans - 1)
