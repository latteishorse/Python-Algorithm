# 1697
# 오작동

import sys
from heapq import heappush, heappop
input = sys.stdin.readline

n, k = map(int,input().split())

graph =[0]*(k+1)

graph[n] = n
graph[k] = k

visited = [False] * (k+1)


def dijkstra():
    heap = []
    heappush(heap, [0, n])
    visited[n] = True

    while heap:
        count, x = heappop(heap)
        dx = [-1, 1]
        mulx = [-2*x,2*x]

        if x == k :
            print(count)
            break

        for i in range(2):
            nx = x + dx[i] 
            tx = x + mulx[i] 
            
            if 0 <= nx < k+1 and not visited[nx] :
                visited[nx] = True
                if graph[nx] == 0:
                    heappush(heap, [count + 1, nx])
                else:
                    heappush(heap, [count, nx])
                    
            elif 0 <= tx < k+1 and not visited[tx]:
                visited[tx] = True
                if graph[tx] == 0:
                    heappush(heap, [count + 1, tx])
                else:
                    heappush(heap, [count, tx])
        
dijkstra()
