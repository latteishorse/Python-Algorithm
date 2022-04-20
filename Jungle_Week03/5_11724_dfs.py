# 11724

# 정점의 개수 N, 간선의 개수 M
# M개의 줄에 양 끝점 u v

# node = 6 , edge = 5
# [1] - 2 5
# [2] - 1 5
# [5] - 1 2
# [3] - 4
# [4] - 3 6

# dfs template
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

def dfs(n):
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


# 11724
cnt = 0

# 모든 노드에 대하여
for i in range(1, n+1):
    # 방문하지 않았다면 = dfs로 돌아가지 않았다면
    if not visited[i]:
        # # 연결된 노드가 없다면
        # if not graph[i] :
        #     cnt += 1
        #     visited[i] = True

        # 연결된 노드가 있다면 dfs 실행
        # else :
        dfs(i)
        cnt += 1

print(cnt)
