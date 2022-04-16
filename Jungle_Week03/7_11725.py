# dfs template
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(n):
    # print(n, end=' ')
    for i in graph[n]:
        if not visited[i]:
            visited[i] = n
            dfs(i)

n = int(input())
graph =[[] for _ in range(n+1)]

for _ in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (n + 1)

# 11725
dfs(1)
for i in range(2, n+1):
    print(visited[i])
