# 1260

# dfs
# 아직 방문하지 않은 노드를
# True, False로 판단 -> 방문한 곳은 True로 바꿔준다
# recursion으로 구현
def dfs(graph, v, visited):
    # 현재 노드를 방문 처리
    visited[v] = True
    print(v, end=' ')
    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)


# stack으로 구현
# def iterative_dfs(v):
#     discovered = []
#     stack = [v]
#     while stack:
#         v = stack.pop()
#         if v not in discovered:
#             discovered.append(v)
#             for w in graph(v):
#                 stack.append(w)
#     return discovered

# # bfs
# def bfs(graph, v):
#     discovered = [v]
#     queue = [v]
#     while queue:
#         for w in graph[queue.pop(0)]:
#             if not discovered:
#                 discovered.append(w)
#                 queue.append(w)
#     return discovered

# --
N, M, V = map(int, input().split())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    graph[a].sort()
    graph[b].sort()

visited = [False] * (N+1)

# dfs(graph, V, visited)
# print()
bfs(graph, V)
print()