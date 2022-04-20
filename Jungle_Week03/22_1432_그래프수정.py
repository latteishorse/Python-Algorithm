# 1432
# https://velog.io/@stthunderl/%EB%B0%B1%EC%A4%80-1432-%EA%B7%B8%EB%9E%98%ED%94%84%EC%88%98%EC%A0%95-python-%EC%9C%84%EC%83%81%EC%A0%95%EB%A0%AC
# https://wonyoung2257.tistory.com/80?category=916963

from heapq import heappop, heappush
import sys
input = sys.stdin.readline

n = int(input())
indegree = [0] * (n+1)

vertex = [[] for _ in range((n+1))]
answer = [0]*(n+1) #
queue = []

# 인접행렬 입력 -> 인접리스트로 변경
for v in range(1, n+1):
  temp = [0]+ list(map(int, input().strip()))
  for i in range(1, n+1):
    if temp[i] == 1:
      vertex[i].append(v)
      indegree[v] += 1

# print(indegree)
# [0, 1, 1, 0, 1, 1]
# print(vertex)
# [[], [], [], [5], [2], [1, 4]]

for i in range(1, n+1):
    if indegree[i] == 0: # 3
    # 최대힙으로  
        heappush(queue,-i) # (q,-3)
  
N = n # 5
while queue:
    now = -heappop(queue) # now = 3
    answer[now] = N # answer[3] = 5

    for i in vertex[now]: # vertex[3] -> 5
        indegree[i] -= 1 # indegree[5] -= 1 -> [0, 1, 1, 0, 1, 0]

        if indegree[i] == 0: # ingegree[5] == 0
            heappush(queue, -i) # q, -5
    N -=1 # n =4
    # print(now, end = ' ')


if answer.count(0) > 1: # index 0번은 0으로 고정이니 1개
  print(-1)
else:
  print(*answer[1:])
