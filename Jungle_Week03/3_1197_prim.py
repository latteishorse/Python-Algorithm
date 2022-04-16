# 1197
# prim algo.

# 1.prim MST algoritm
import sys
import heapq
input = sys.stdin.readline
 
# vertex, edge 
V, E = map(int, input().split())

# 방문 여부를 확인
visited = [False]*(V+1)

# edge를 저장
Elist = [[] for _ in range(V+1)]

# 현재 그래프에서 짧은 경로를 선택
heap = [[0, 1]]
for _ in range(E):
    s, e, w = map(int, input().split())
    Elist[s].append([w, e])
    Elist[e].append([w, s])
 
answer = 0
cnt = 0
while heap:
    if cnt == V:
        break
    w, s = heapq.heappop(heap)
    if not visited[s]:
        visited[s] = True
        answer += w
        cnt += 1
        for i in Elist[s]:
            heapq.heappush(heap, i)
 
print(answer)