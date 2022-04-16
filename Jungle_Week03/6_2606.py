# dfs template
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)
count = 0

def dfs(n):
    global count
    visited[n] = True
    for i in graph[n]:
        if not visited[i]:
            count += 1
            dfs(i)

n = int(input())
m = int(input())

graph =[[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (n + 1)

# 2606
dfs(1)
print(count)