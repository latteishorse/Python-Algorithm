# 21606
import sys

# dfs template
sys.setrecursionlimit(10000)

def dfs(n):
    # print(n, end=' ')
    visited[n] = True
    for i in graph[n]:
        if not visited[i]:
            dfs(i)

n = int(input())
side = list(str(input()))

graph =[[] for _ in range(n+1)]

for _ in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (n + 1)
