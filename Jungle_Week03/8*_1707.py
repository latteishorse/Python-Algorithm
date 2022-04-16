# # 변별 알고리즘
# 주어진 그래프가 이분 그래프인지 확인하는 것은 어렵지 않다. 
# 그래프의 꼭짓점들을 깊이 우선 탐색으로 나열한 뒤, 
# 각 꼭짓점들을 이웃 꼭짓점들과 다른 색으로 계속해서 칠해 나가면서, 
# 같은 색깔의 꼭짓점이 서로 연결되어 있는 모순이 발생하는지 여부를 확인하면 된다. 
# 이 알고리즘은 O(|V|+|E|)이다.

# https://ko.wikipedia.org/wiki/%EC%9D%B4%EB%B6%84_%EA%B7%B8%EB%9E%98%ED%94%84

# dfs template
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(n):
    # print(n, end=' ')
    visited[n] == 1
    for i in graph[n]:
        
        if visited[i] == 0:

            dfs(i)

tc = int(input())

for _ in range():
    v, e = map(int, input().split())

    graph =[[] for _ in range(v+1)]


    for _ in range(v):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    visited = [0] * (v + 1)

    for i in range(v):
        print(visited[i])
