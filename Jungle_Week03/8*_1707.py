# # 변별 알고리즘
# 주어진 그래프가 이분 그래프인지 확인하는 것은 어렵지 않다. 
# 그래프의 꼭짓점들을 깊이 우선 탐색으로 나열한 뒤, 
# 각 꼭짓점들을 이웃 꼭짓점들과 다른 색으로 계속해서 칠해 나가면서, 
# 같은 색깔의 꼭짓점이 서로 연결되어 있는 모순이 발생하는지 여부를 확인하면 된다. 
# 이 알고리즘은 O(|V|+|E|)이다.

# https://ko.wikipedia.org/wiki/%EC%9D%B4%EB%B6%84_%EA%B7%B8%EB%9E%98%ED%94%84

import sys
# 문제 조건 20000
sys.setrecursionlimit(20000)
input = sys.stdin.readline

def dfs(start, group):
    global error

    # 만약 사이클이 true라면 재귀탈출
    if error:
        return

    # ex) visited[1] = 1
    # visited[3] = -1
    visited[start] = group  # 해당 그룹으로 등록

    # graph[1] - > 3
    # graph[3] -> 1, 2
    for i in graph[start]:

        if not visited[i]:
            dfs(i, -group)  # 다른 그룹으로 설정

        #dfs(3, -1)
        #dfs(2, 1)

        elif visited[start] == visited[i]:  # 인접한데 같은 그룹이라면

            error = True  # 에러값 True
            return  # 그후 재귀 리턴

TC = int(input())

for _ in range(TC):
    # 2번째줄 입력
    V, E = map(int, input().split())

    graph = [[] for _ in range(V + 1)]  # 빈 그래프 생성
    # 
    visited = [False] * (V + 1)  # 방문한 정점 체크
    error = False

    for _ in range(E):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    for i in range(1, V + 1):
        if not visited[i]:  # 만약 아직 방문하지 않았다면

# group 1 => 초기 그룹
            dfs(i, 1)  # dfs를 돈다.

            if error:  # 만약 에러가 참이라면
                break  # 탈출

    if error:
        print('NO')
        
    else:
        print('YES')

# print( if result else )