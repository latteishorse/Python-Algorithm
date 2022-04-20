from sys import stdin, setrecursionlimit
setrecursionlimit(10 ** 9)
input = stdin.readline

def dfs(node):
    visited[node] = True
    global cnt
    # 그래프에 입력한 노드 하나씩 꺼내옴
    for i in graph[node]:
        #  실내
        if A[i] == 1:
            # 카운트 + 1
            cnt += 1
        elif not visited[i]:
            # 방문하지 않았고, 실내일 경우
            # 재귀로 한단계 더 내려감
            cnt = dfs(i)

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

for i in range(2, N + 1):
    if A[1] == 1:
        for j in graph[1]:
            if A[j] == 1:
                cnt += 1

    elif A[i] == 1:
        for j in graph[i]:
            if A[j] == 1:
                cnt += 1
    else:
        if A[i] == 0 and not visited[i]:
            x = dfs(i)
            cnt += x*(x-1)
        
print(cnt)