# 18352
# 다익스트라

# 도시의 개수 N, 도로의 개수 M
# 거리 정보 k, 출발 도시의 번호 X

# A -> B
import sys
from heapq import heappop, heappush

input = sys.stdin.readline
inf = sys.maxsize

n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n+1)]

dp = [inf] * (n+1)
heap = []


def dijkstra(start):
    heappush(heap, [0, start])

    dp[start] = 0
    while heap:
        w, n = heappop(heap)
        for n_n, wei in graph[n]:
            n_w = wei + w
            if n_w < dp[n_n]:
                dp[n_n] = n_w
                heappush(heap, [n_w, n_n])


for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append([b, 1])

dijkstra(x)
ans = []

for i in range(1, n + 1):
    if dp[i] == k:
        ans.append(i)

if ans:
    for i in ans:
        print(i)
else:
    print(-1)










# 1197
# prim MST algoritm
import heapq
import sys; input=sys.stdin.readline

def prim(start, cost):
    # prim(1, 0)
    # 방문 확인 리스트 만듦
    visit = [0] * (V + 1) 

    # 힙 구조를 사용하기 위해 가중치를 앞에 둠
    q = [[cost, start]] 

    ans = 0 # 가중치 합
    cnt = 0 # 간선의 개수

    while cnt < V: # 간선의 개수 최대는 V-1
        
        k, v = heapq.heappop(q)

        if visit[v]: 
            continue 
        visit[v] = 1 
        ans += k
        cnt += 1 

        for u, c in G[v]: 
            heapq.heappush(q, [c, u])

    return ans

V, E = map(int, input().split())
G = [[] for _ in range(V + 1)]
for _ in range(E):

    u, v, c = map(int, input().split())
    G[u].append([v, c])
    G[v].append([u, c])
print(prim(1, 0))