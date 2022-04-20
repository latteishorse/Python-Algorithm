from sys import stdin, setrecursionlimit
setrecursionlimit(10 ** 9)
input = stdin.readline

def dfs(node, cnt):
    visited[node] = True
    
    for i in graph[node]:
        if A[i] == 1:
            cnt += 1
        elif not visited[i] and A[i] == 0:
            cnt = dfs(i, cnt)
    return cnt

N = int(input())
A = [0] + list(map(int, input().strip()))
graph = [[] for _ in range(N + 1)]
visited = [False] * (N + 1)

cnt = 0
result = 0

for _ in range(N - 1):
    start, end = map(int, input().split())
    graph[start].append(end)
    graph[end].append(start)

for i in range(1, N + 1):
    if A[i] == 1:
        for j in graph[i]:
            if A[j] == 1:
                cnt += 1
    else:
        # if A[i] == 0 and not visited[i]:
        if i not in visited:
            x = dfs(i, cnt)
            cnt += x*(x-1)
        
print(cnt)