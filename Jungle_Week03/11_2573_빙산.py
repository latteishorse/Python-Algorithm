n, m = map(int, input().split())
data = [list(map(int,input().split())) for _ in range(n)]

# 방문 내역 저장용 visited
visited = [[0]*m for _ in range(n)]
graph = [[]]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
# 해당 위치에서
# 몇개의 0을 인접해 있는지 판단해야됨

# 현재 위치 수 -  인접 0 수
# 0이하면 0으로 처리
def count_zero(x,y):
    global cnt
    cnt = 0
    for i in range(4):
        nx,ny = x+dx[i],y+dy[i]
        if 0<=nx<n and 0<=ny<m and data[nx][ny]==0:
            cnt += 1
    return cnt

nums = 0
def bfs(x,y):
    global nums
    visited[x][y] = 1

    if graph[x][y] >= 1:
        nums += 1
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            if visited[nx][ny] == 0 and graph[nx][ny] >= 1:
                bfs(nx,ny)
        
print(nums)

# ---

if count_zero():
    print(cnt)
    exit()

bfs()