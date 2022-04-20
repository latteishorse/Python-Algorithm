#https://wookcode.tistory.com/155?category=1008519

from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int,input().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

queue = deque()
check = False
day = 0

def bfs(a,b):
    queue.append((a,b))
    while queue:
        x,y = queue.popleft()
        visited[x][y] = True

        for i in range(4): # 상하좌우 이동시켜봄
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m: # 범위 내에서
                if graph[nx][ny] != 0 and not visited[nx][ny]: 
                    visited[nx][ny] = True
                    queue.append((nx,ny))
                elif graph[nx][ny] == 0:    # 주변이 0이면
                    count[x][y] += 1
     # 몇번 이동했는지               
    return 1 # result에 1을 넣어줘서 녹았는지 판단


# 빙산이 분리될때까지 돌아줌
while True:
    visited = [[False]*m for _ in range(n)]
    count = [[0] * m for _ in range(n)]
    result = [] # result를 매번 초기화

    for i in range(n):  
        for j in range(m):
            if graph[i][j] != 0 and visited[i][j] == False: # 다 녹지 않았고, 방문하지 않았으면 bfs를 돌려주는데 결과값을 result에 넣음
                result.append(bfs(i,j))
    # print(result, '1')

    # melt           
    for i in range(n):  
        for j in range(m):
            graph[i][j] -= count[i][j] # count 된 만큼 -해줌

            if graph[i][j] < 0: # 최저값 0으로 고정
                graph[i][j] = 0
    # print(result, '2')
    
    if len(result) == 0: # 빙산이 다없어질때까지 분리가 되지않으면 break
        print(0)
        break

    if len(result) >= 2: # 빙산이 분리되면 break
        check = True
        break
    day += 1

if check:        
    print(day)