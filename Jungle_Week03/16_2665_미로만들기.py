# # 1665
# from collections import deque
# from pprint import pprint
# n = int(input())

# graph = [list(map(int, input())) for _ in range(n)]
# pprint(graph)

# visited = [[False]* n for _ in range(n)]
# visited[0][0] = True

# queue = deque([[0,0]])
# count_graph = [[0]*n for _ in range(n)]

# cnt = 0
# dy = [-1,1,0,0]
# dx = [0,0,-1,1]

# while queue:
#     y, x = queue.popleft()

#     if x == n and y == n:
#         break
#     for i in range(4):
#         nX = x + dx[i]
#         nY = y + dy[i]

#         if 0 <= nX < n and 0 <= nY < n:
#             if graph[nY][nX] == 1 and not visited[nY][nX]: #  이동할 수 있는 칸이고 ,방문하지 않았다면
#                 visited[nY][nX] = True # 방문 체크
#                 queue.append([nY, nX]) # 큐에 해당 위치 append                
#                 count_graph[nY][nX] += count_graph[y][x] + 1 # 지금 위치까지 이동값 + 1 을 새로운 위치의 이동값으로 저장
#             elif graph[nY][nX] == 0: #  이동할 수 있는 칸이고 ,방문하지 않았다면
#                 graph[nY][nX] == 1
#                 visited[nY][nX] = True # 방문 체크

#                 queue.append([nY, nX]) # 큐에 해당 위치 append                
#                 count_graph[nY][nX] += count_graph[y][x] + 1 # 지금 위치까지 이동값 + 1 을 새로운 위치의 이동값으로 저장
#                 # cnt += 1
#                 # print(queue)
#                 # print(cnt)

# print(cnt)
# -------------

import sys
from heapq import heappush, heappop

input = sys.stdin.readline
n = int(input())
maze = []
for _ in range(n):
    maze.append(list(map(int, input().strip())))
visit = [[False] * n for _ in range(n)]

def dijkstra():
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]
    heap = []
    heappush(heap, [0, 0, 0])

    visit[0][0] = True

    while heap:
        count, x, y = heappop(heap)

        if x == n - 1 and y == n - 1:
            print(count)
            break

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and not visit[nx][ny]:

                visit[nx][ny] = True
                if maze[nx][ny] == 0:
                    heappush(heap, [count + 1, nx, ny])
                else:
                    heappush(heap, [count, nx, ny])

dijkstra()

