# prim MST algoritm 변형

# 아이디어
# 프림 알고리즘 : 최소힙으로 최소값 계산
# 최대힙으로 계산하면 최대 트리를 만들 수 있지 않을까?
# 가중치가 최대가 될때, 또는 노드 방문이 최대가 될 때를 판단할 수 있을 것으로 예상

# 위상 정렬로 정렬하고
# 프림 응용 최대힙 -> 최대 비용 순, 최대 도시 순으로 정렬하면 되지 않을까?

from heapq import heappush, heappop
# import sys; input=sys.stdin.readline

def prim(start, cost):
    visit = [0] * (V + 1) 
    # 힙 구조를 사용하기 위해 가중치를 앞에 둠
    q = [[cost, start]] 
    ans = 0 # 가중치 합
    cnt = 0 # 간선의 개수

    while cnt < V: # 간선의 개수 최대는 V-1
        k, v = heappop(q)
        if visit[v]: 
            continue 
        visit[v] = 1 
        ans += k 
        cnt += 1 
   
        for u, c in G[v]: # 해당 정점의 간선정보를 불러옴
            heappush(q, [c, u]) # 힙에 넣어줌

    return -ans

V, E = map(int, input().split())
G = [[] for _ in range(V + 1)]
for _ in range(E):

    u, v, c = map(int, input().split())
   
    G[u].append([v, -c])
    G[v].append([u, -c])

print(prim(1, 0))