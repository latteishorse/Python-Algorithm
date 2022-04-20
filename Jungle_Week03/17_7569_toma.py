
# from collections import deque

# m, n, h = map(int, input().split())
# # matrix = [list(map(int, input().split())) for _ in range(n*h)]
# matrix = []
# queue = deque([])

# # 축 정렬
# dx = [-1, 1, 0, 0, 0, 0]
# dy = [0, 0, -1, 1, 0, 0]
# dz = [0, 0, 0, 0, 1, -1]

# ans = 0

# for i in range(h):
#     tmp = []
#     for j in range(n):
#         tmp.append(list(map(int, input().split())))

#         for k in range(m):
#             if tmp[j][k] == 1:
#                 queue.append([i, j, k])
#     matrix.append(tmp)


# while queue:
#     x, y, z = queue.popleft()

#     for i in range(6):
#         nx = dx[i] + x
#         ny =  dy[i] + y
#         nz = dz[i] + z

#         if 0 <= nx < h and 0 <= ny < n and 0 <= nz < m and matrix[nx][ny][nz] == 0:
#             matrix[nx][ny][nz] = matrix[x][y][z] + 1
#             queue.append([nx, ny, nz])


# for i in matrix:
#     for j in i:
#         for k in j:
#             if k == 0:
#                 print(-1)
#                 exit(0)
#         ans = max(ans, max(i))
# print(ans - 1)

# # ---
# import sys
# from collections import deque
# m,n,h = map(int,input().split()) # mn크기, h상자수
# graph = []
# queue = deque([])
 
# for i in range(h):
#     tmp = []
#     for j in range(n):
#         tmp.append(list(map(int,sys.stdin.readline().split())))
#         for k in range(m):
#             if tmp[j][k]==1:
#                 queue.append([i,j,k])
#     graph.append(tmp)
    
# dx = [-1,1,0,0,0,0]
# dy = [0,0,1,-1,0,0]
# dz = [0,0,0,0,1,-1]
# while(queue):
#     x,y,z = queue.popleft()
    
#     for i in range(6):
#         a = x+dx[i]
#         b = y+dy[i]
#         c = z+dz[i]
#         if 0<=a<h and 0<=b<n and 0<=c<m and graph[a][b][c]==0:
#             queue.append([a,b,c])
#             graph[a][b][c] = graph[x][y][z]+1
            
# day = 0
# for i in graph:
#     for j in i:
#         for k in j:
#             if k==0:
#                 print(-1)
#                 exit(0)
#         day = max(day,max(j))
# print(day-1)
 
# ----

import sys
from collections import deque
input = sys.stdin.readline

m,n,h = map(int,input().split())

dx = [-1,1,0,0,0,0]
dy = [0,0,-1,1,0,0]
dz = [0,0,0,0,-1,1]

matrix = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]
queue = deque()

def tomatomatotomamahatetomamatotoamtomatoma():
    while queue:
        z,x,y = queue.popleft()
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]
            if 0 <= nx < n and 0 <= ny < m and 0 <= nz < h:
                if matrix[nz][nx][ny] == 0:
                    matrix[nz][nx][ny] = matrix[z][x][y]+1
                    queue.append((nz,nx,ny))
            
for i in range(h):
    for j in range(n):
        for k in range(m):
            if matrix[i][j][k] == 1:
                queue.append((i,j,k))

tomatomatotomamahatetomamatotoamtomatoma()
# print(queue)
# print(matrix)

result = 0
for i in range(h):
    for j in range(n):
        for k in range(m):
            if matrix[i][j][k] == 0:
                print(-1)
                exit()
            result = max(result,matrix[i][j][k])

print(result-1)