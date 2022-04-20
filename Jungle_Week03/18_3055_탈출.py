#https://www.acmicpc.net/board/view/80536
# https://dapsu-startup.tistory.com/entry/%EB%B0%B1%EC%A4%80-%ED%83%88%EC%B6%9C-3055-%ED%8C%8C%EC%9D%B4%EC%8D%ACPython

from collections import deque

R, C = map(int, input().split())

graph = [list(input()) for _ in range(R)]
visited = [[False] * C for _ in range(R)]

sonic = deque()  
water = deque() 
count = 0  

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(R):
    for j in range(C):
        # 물
        if graph[i][j] == '*':
            water.append((i, j))
            visited[i][j] = True
        # 소닉
        elif graph[i][j] == 'S':
            sonic.append((i, j))
            visited[i][j] = True
        # 막힌길
        elif graph[i][j] == 'X':
            visited[i][j] = True # 방문처리하고 시작해서 막아버림

while sonic:
    for _ in range(len(water)):
        w_x, w_y = water.popleft() # 물 먼저 채움

        for i in range(4):
            nx = w_x + dx[i]
            ny = w_y + dy[i]
            if 0 <= nx < R and 0 <= ny < C:

                if graph[nx][ny] == '.': # 물 옆으로 채워줌
                    water.append((nx, ny))

                    graph[nx][ny] = '*' # 물 방문 처리하고
                    visited[nx][ny] = True

    count += 1 # 

    for _ in range(len(sonic)):
        s_x, s_y = sonic.popleft() # 소닉 무빙

        for i in range(4):
            nx = s_x + dx[i]
            ny = s_y + dy[i]

            if 0 <= nx < R and 0 <= ny < C: # 
                if graph[nx][ny] =='.' and visited[nx][ny] == False: 
                    sonic.append((nx, ny)) # 아직 물 안찬 곳으로 소닉 이동
                    visited[nx][ny] = True 

                elif graph[nx][ny] == 'D': # 골이면
                    print(count)    # 카운트된 횟수 프린트하고
                    exit() # 출력해버림

print('KAKTUS')
