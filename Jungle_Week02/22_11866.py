# 11866
# import sys
# from collections import deque
# input = sys.stdin.readline

# n, k = map(int, input().split())
# qList = list(range(1, n+1))
# outQueue = deque([])

# for i in range(1,n):
#     ans = (3 * i) % 7 -1
#     outQueue.append(qList[ans])
#     qList.pop()

# print(outQueue)
# ---
# 제외되는 인원을 빼고 3번째를 카운트
import sys
input = sys.stdin.readline
from collections import deque
n, k = map(int, input().split())
qu = deque()

for i in range(1, n+1):
    qu.append(i)

print('<', end='')
while qu:
    for _ in range(k-1):
        qu.append(qu.popleft())
    print(qu.popleft(), end='')
    if qu:
        print(',', end=' ')
print('>')

#-----
