from collections import deque
import sys
input = sys.stdin.readline

n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n+1)]

distance = [0] * (n+1)
visited = [False] * (n+1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b) # 단방향

    # graph[b].append(a)

def bfs(start): # x부터 출발
    answer = []
    q = deque([start]) 

    visited[start] = True
    distance[start] = 0

    while q:
        # x
        now = q.popleft() # 현재 위치 pop

        # graph[x]
        for i in graph[now]: # 현재 노드와 연결된 노드 중
            if not visited[i]: # 아직 방문하지 않은 곳
                visited[i] = True # 방문처리
                q.append(i) # 큐에 i값 append

                # 현재 노드에서 i 노드까지 가는 거리 + 1
                distance[i] = distance[now] + 1 

                # 최단거리 K
                # i번째 거리가 k가 되면
                if distance[i] == k:
                    answer.append(i) # 해당 도시 번호를 answer에 append

    if not answer:
        print(-1)
    else:
        answer.sort()
        for i in answer:
            print(i)

bfs(x)