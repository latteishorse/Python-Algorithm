# 오작동

from collections import deque
N = int(input())
graph = [list(map(int, input())) for _ in range(N)]

# graph와 동일한 크기의 배열 생성
# count_graph = [[0]*N for _ in range(N)]

visited = [[False]*N for _ in range(N)]

queue = deque([[0, 0]])
visited[0][0] = True
# 첫 위치 1
# count_graph[0][0] = 1

# 상 하 좌 우
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
cnt = 0

while queue:
    # 0 ,0 pop
    y, x = queue.popleft()

    if x == N-1 and y == N-1:       # -> 끝까지 갔으면 
        print(cnt)
        break                   # break

    for i in range(4):          # 상하좌우 => range(4)
        nX = x + dx[i]          
        nY = y + dy[i]
        # 상, 하, 좌, 우
        # 한칸씩 이동시켜 봄

        if 0 <= nX < N and 0 <= nY < N and not visited[nY][nX]: # 아직 이동할 칸이 남아있다면
            if graph[nY][nX] == 1 : #  이동할 수 있는 칸이고 ,방문하지 않았다면
                visited[nY][nX] = True # 방문 체크
                queue.append([nY, nX]) # 큐에 해당 위치 append
            elif graph[nY][nX] == 0:
                visited[nY][nX] = True # 방문 체크
                queue.append([nY, nX]) # 큐에 해당 위치 append
                cnt += 1

# print(cnt)
# print(count_graph)
