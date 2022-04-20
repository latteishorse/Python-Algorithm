# 1916

import sys, heapq
input = sys.stdin.readline
INF = 987654321

# 도시 개수 n, 버스 개수 m
n = int(input())
m = int(input())

graph = [[] for _ in range(n+1) ]

for _ in range(m):
    start,end,cost = map(int,input().split())
    graph[start].append((cost,end))

cityStart, cityEnd = map(int,input().split())

dist = [INF] * (n+1)

def dijkstra(startNode):
    dist[startNode] = 0 # 출발 노드 거리 0
    q = [(0,startNode)] # (0,1)

    while q:
        curCost, curNode = heapq.heappop(q)

        if dist[curNode] < curCost : # 제외 안해주면 시간초과
            continue
        
        for nextCost, nextNode in graph[curNode]:
            if dist[nextNode] > curCost + nextCost:
                dist[nextNode] = curCost + nextCost

                heapq.heappush(q, (dist[nextNode], nextNode))

        # for next_cost, next_node in graph[cur_node]: # 현재 노드와 연결된 노드와 비용
            
        #     if dist[next_node] > cur_cost + next_cost: # 
        #         dist[next_node] = cur_cost + next_cost # 다음 노드까지 비용을 현재 비용과 현재에서 다음으로 넘어가는 비용을 더한 값으로 변경
        #         heapq.heappush(q, (dist[next_node],next_node))  # 연결값 갱신
    return dist

answer = dijkstra(cityStart)
# 도작 지점의 최소 비용
print(answer[cityEnd])