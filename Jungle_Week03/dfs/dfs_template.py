# dfs template
import sys
input = sys.stdin.readline
# sys.setrecursionlimit(10000)

def dfs(n):
    # print(n, end=' ')
    visited[n] = True
    for i in graph[n]:
        if not visited[i]:
            dfs(i)

n, m = map(int, input().split())
graph =[[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (n + 1)
