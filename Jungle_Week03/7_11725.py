# dfs template
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(n):
    # print(n, end=' ')
    for i in graph[n]:
        # not을 판단하므로 True 말고 다른 값 넣어도 됨
        if not visited[i]:
            # dfs(n)이 dfs(i) 의 부모 노드
            # 따라서 부모 노드 저장
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

# 부모 노드를 2번부터 순서대로 출력

for i in range(2, n+1):
    print(visited[i])
