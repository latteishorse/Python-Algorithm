# 2178
 # 미로탐색

# # import sys
# from collections import deque
# # input = sys.stdin.readline

# N, M = map(int,input().split())
# graph = []

# for _ in range(N):
#     graph.append(list(map(int, input())))

# dx = [-1,1,0,0]
# dy = [0,0,-1,1]

# visited = [[] for _ in range(N+1)]

# q = deque([(0, 0)])
# 방문한 곳을 1로 변경
# visited[0][0] = 1

# # queue에 append 된 값이 있는 동안
# while q:
#     # 하나씩 pop
#     x, y = q.popleft()

#     # 미로의 끝에 도달 했을 때 해당 미로의 값을 호출
#     if x == N-1 and y == M-1:
#         print(visited[x][y])
    
#     for i in range(4):
#         nx, ny = x + dx[i], y + dy[i]

#         if 0 <= nx < N and 0 <= ny < M:
#             if visited[nx][ny] == 0 and graph[nx][ny] == 1:
#                 visited[nx][ny] = visited[x][y] + 1
#                 q.append((nx, ny))
# # ---

from collections import deque
N, M = map(int, input().split())
graph = [list(map(int, input())) for _ in range(N)]

# graph와 동일한 크기의 배열 생성
count_graph = [[0]*M for _ in range(N)]
visited = [[False]*M for _ in range(N)]

queue = deque([[0, 0]])
visited[0][0] = True

# 첫 위치 1
count_graph[0][0] = 1

# 상 하 좌 우
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

while queue:
    # 0 ,0 pop
    y, x = queue.popleft()

    if x == M-1 and y == N-1:   # -> 끝까지 갔으면 
        break                   # break

    for i in range(4):          # 상하좌우 => range(4)
        nX = x + dx[i]          
        nY = y + dy[i]
        # 상, 하, 좌, 우
        # 한칸씩 이동시켜 봄

        if 0 <= nX < M and 0 <= nY < N: # 아직 이동할 칸이 남아있다면
            if graph[nY][nX] == 1 and not visited[nY][nX]: #  이동할 수 있는 칸이고 ,방문하지 않았다면
                visited[nY][nX] = True # 방문 체크
                queue.append([nY, nX]) # 큐에 해당 위치 append

                count_graph[nY][nX] += count_graph[y][x] + 1 # 지금 위치까지 이동값 + 1 을 새로운 위치의 이동값으로 저장

# # print(count_graph)
print(count_graph[N-1][M-1])

# # ---
# N, M = map(int, input().split())
# graph = [list(map(int, input())) for _ in range(N)]

# # graph와 동일한 크기의 배열 생성
# count_graph = [[0]*M for _ in range(N)]

# visited = [[False]*M for _ in range(N)]

# stack = [[0, 0]]
# visited[0][0] = True
# # 첫 위치 1
# count_graph[0][0] = 1

# # 상 하 좌 우
# dy = [-1, 1, 0, 0]
# dx = [0, 0, -1, 1]

# while stack:
#     # 0 ,0 pop
#     y, x = stack.pop()

#     if x == M and y == N:       # -> 끝까지 갔으면 
#         break                   # break

#     for i in range(4):          # 상하좌우 => range(4)
#         nX = x + dx[i]          
#         nY = y + dy[i]
#         # 상, 하, 좌, 우
#         # 한칸씩 이동시켜 봄

#         if 0 <= nX < M and 0 <= nY < N: # 아직 이동할 칸이 남아있다면
#             if graph[nY][nX] == 1 and not visited[nY][nX]: #  이동할 수 있는 칸이고 ,방문하지 않았다면
#                 visited[nY][nX] = True # 방문 체크
#                 stack.append([nY, nX]) # 큐에 해당 위치 append
                
#                 count_graph[nY][nX] += count_graph[y][x] + 1 # 지금 위치까지 이동값 + 1 을 새로운 위치의 이동값으로 저장

# # print(count_graph)
# print(count_graph[N-1][M-1])

# # ----