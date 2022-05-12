# 11286
'''
배열에 정수 x (x ≠ 0)를 넣는다.

배열에서 절댓값이 가장 작은 값을 출력하고, 그 값을 배열에서 제거한다. 절댓값이 가장 작은 값이 여러개일 때는, 가장 작은 수를 출력하고, 그 값을 배열에서 제거한다.
'''

import sys; input = sys.stdin.readline
from heapq import heappush, heappop

n = int(input())
heap = []

for _ in range(n):
    num = int(input())
    if num:
        heappush(heap, (abs(num), num))
    else:
        try:
            print(heappop(heap)[1])
        except:
            print(0)
