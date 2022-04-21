# 1939
# 예제 정상 출력, 오답

import sys
from heapq import heappop, heappush
input = sys.stdin.readline
inf = 987654321

def dijkstra(start):
    heappush(heap, [0, start])

    road[start] = 0
    while heap:
        w, n = heappop(heap)
        for newn, we in graph[n]:
            mergeW = we + w
            if mergeW < road[newn]:
                road[newn] = mergeW
                heappush(heap, [mergeW, newn])


n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
road = [inf] * (n+1)
heap = []

for _ in range(m):
    a, b, c  = map(int, input().split())
    graph[b].append([c, a])

start, end = map(int, input().split())
dijkstra(start)
ans = []

for i in range(1, n + 1):
    if road[i] == end:
        ans.append(i)

print(*ans)

