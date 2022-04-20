import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())

inDegree = [ 0 for _ in range(32001)]
graph = [[] for _ in range(32001)]
queue = deque()

for i in range(m):
    a, b = map(int, input().split())
    inDegree[b] += 1
    graph[a].append(b)

for i in range(1, n + 1):
    if inDegree[i] == 0:
        queue.append(i)

while queue:
    student = queue.popleft()

    for i in graph[student]:
        inDegree[i] -= 1

        if inDegree[i] == 0:
            queue.append(i)
    print(student, end = ' ')
