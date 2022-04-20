# 1197
# prim MST algoritm
from heapq import heappush, heappop
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
        
        # heap 이므로 최소순으로 정렬 
        k, v = heappop(q)
        # 0,1

        # 1,2

        # visited True (1)
        # visit[1]

        # visit[2]

        # visit[3]

        if visit[v]: 
            continue # 이미 방문한 정점이면 지나감

        visit[v] = 1 # 방문안했으면 방문처리

        ans += k # 해당 정점까지의 가중치를 더해줌
        # ans = 1
        # ans = 2

        cnt += 1 # 간선의 갯수 더해줌
        # cnt = 2
        # cnt = 3

        # for u,c in G[1]
        # [2,1],[3,3]

        # for u,c in G[2]
        # [1,1],[3,3]

        for u, c in G[v]: # 해당 정점의 간선정보를 불러옴
            heappush(q, [c, u]) # 힙에 넣어줌

            # q = [[1, 2],[3,3]]
            # cnt = 1

            # q = [[3,3], [1,1], [3,3]]
            # cnt = 2

            # 

    return ans

V, E = map(int, input().split())
G = [[] for _ in range(V + 1)]
for _ in range(E):

    u, v, c = map(int, input().split())
    # 1 2 1
    # 2 3 2
    # 1 3 3
    G[u].append([v, c])
    # G[1] append [2,1]
    # G[2] append [3,2]
    # G[1] append [3,3]
    # G = [[[2,1],[3,3]], [3,3]]

    G[v].append([u, c])
    # G[2] append [1,1]
    # G[3] append [2,2]
    # G[3] append [1,3]
 
    # G = [[[2,1],[3,3]], [[1,1],[3,3]], [[1,3],[2,2]]]

# start = 1
# cost = 0

# 정점 번호 1번부터 매겨져 있음
print(prim(1, 0))