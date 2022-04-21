# 18405
from collections import deque

n, k = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
s, x, y  = map(int, input().split())

visited = [[False] * n for _ in range(n)]

numbers = deque()
cnt = s

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for k in range(1,k+1):
    for i in range(n):
        for j in range(n):
                if graph[i][j] == k:
                    numbers.append([i, j])
                    visited[i][j] = True

while cnt > 0 :
    for _ in range(len(numbers)):
        px, py = numbers.popleft() 
        for i in range(4):
            nx = px + dx[i]
            ny = py + dy[i]
            if 0 <= nx < n and 0 <= ny < n:

                if graph[nx][ny] == 0: 
                    numbers.append((nx, ny))

                    graph[nx][ny] = graph[px][py] 
                    visited[nx][ny] = True
    cnt -= 1

if not visited[x-1][y-1]:
    print(0)
else:
    print(graph[x-1][y-1])
