# bfs template
import sys
from collections import deque
input = sys.stdin.readline

def bfs(n):
    visited[n] = True
    queue = deque([n])
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

n, m = map(int, input().split())
graph =[[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (n + 1)

# 11724
cnt = 0
# 모든 노드에 대하여
for i in range(1, n+1):
    # 방문하지 않았다면 = bfs로 돌아가지 않았다면
    if not visited[i]:
        bfs(i)
        cnt += 1

print(cnt)
