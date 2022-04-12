# 2164
import sys
from collections import deque
input = sys.stdin.readline

# 배열 회전
n = int(input())
q = deque([])

for i in range(1,n+1):
    q.append(i)

for _ in range(n-1):
    q.popleft()
    q.append(q.popleft())

for i in q:
    print(i)

# 더 깔끔한 코드
from collections import deque
N = int(input())

queue = deque(range(1, N+1))

while len(queue) != 1:
    queue.popleft()
    queue.append(queue.popleft())
    
print(queue[0])