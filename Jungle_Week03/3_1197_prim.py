# 1197
# prim algo.
# # 1.prim MST algoritm
# import sys, heapq
# input = sys.stdin.readline
 
# # vertex, edge 
# V, E = map(int, input().split())

# # 방문 여부를 확인
# visited = [False]*(V+1)

# # edge를 저장
# Elist = [[] for _ in range(V+1)]

# # 현재 그래프에서 짧은 경로를 선택
# # 시작 지점 0
# heap = [[0, 1]]

# # v, v, 가중치
# for _ in range(E):
#     # 
#     s, e, w = map(int, input().split())
#     # 가중치 저장
#     Elist[s].append([w, e])
#     Elist[e].append([w, s])

# answer = 0
# cnt = 0

# while heap:
#     # 정점 수
#     if cnt == V:
#         break
#     w, s = heapq.heappop(heap)
#     if not visited[s]:
#         visited[s] = True
#         answer += w
#         cnt += 1
# # 
#         for i in Elist[s]:
#             heapq.heappush(heap, i)
 
# print(answer)
# # ---
# 방문한 정점들에 연결된 간선 중 가중치가 가장 작은 간선부터 연결시키는 알고리즘

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

        if visit[v]: 
            continue # 이미 방문한 정점이면 지나감

        visit[v] = 1 # 방문안했으면 방문처리

        ans += k # 해당 정점까지의 가중치를 더해줌
        cnt += 1 # 간선의 갯수 더해줌
        for u, c in G[v]: # 해당 정점의 간선정보를 불러옴
            heappush(q, [c, u]) # 힙에 넣어줌
    return ans

V, E = map(int, input().split())
G = [[] for _ in range(V + 1)]
for _ in range(E):

    u, v, c = map(int, input().split())

    G[u].append([v, c])
    G[v].append([u, c])

print(prim(1, 0))