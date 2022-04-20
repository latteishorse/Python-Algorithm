
# 5 
# 1번 2개
# 2번 2개
# 6
# 5번 2개 = 1번 4개, 2번 4개
# 3번 3개
# 4번 4개

# 7
# 6번 3개 = 1번 12개, 2번 12개, 3번 9개 4번 12개
# 5번 2개
# 4번 5개

# -> 큰 조립품 -> 작은 하위 조립품으로 나눠서 
import time
# ------


# ------

import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
m = int(input())

inDegree = [ 0 for _ in range(n+1)]
graph = [[] for _ in range(n+1)]
queue = deque()

for i in range(m):
    a, b, c = map(int, input().split())
    inDegree[b] += 1
    graph[a].append([b,c])

start_time = time.time()


# for i in range(1, n + 1):
#     if inDegree[i] == 0:
#         for j in inDegree[i]:
#             graph[j[0]] += j[1] * graph[i]

# indegree i번째 뽑아내면
# 거기 조립하는데 필요한건
# graph에 들어있음
# graph 에서 첫 수 -> 부품 번호
# 두번째 수 -> 수량
# 해당 부품 필요 수량으로 업로드 해주면 됨

# for i in inDegree:
# for i in range()
print(graph)
print(inDegree)

for i in range(n):
    for j in len(graph[i]):
        gear = graph[i][j][0]
        gearNum = graph[i][j][1]
        inDegree[gear] += gearNum
        inDegree[i] -= 1

print(inDegree)
end_time = time.time()
print("time :", end_time - start_time)
# gearNumber = graph[6][0][0]


# inDegree[gearNumber] += graph[6][0][1]
# 넣고 기존 리스트 팝시킴

# print(graph)
# # print(inDegree)
# # print(gear)
# # print(gearNum)

# while queue:
#     student = queue.popleft()

#     for i in graph[student]:
#         inDegree[i] -= 1

#         if inDegree[i] == 0:
#             queue.append(i)
#     print(student, end = ' ')
