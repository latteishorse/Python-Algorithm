# 11279
'''
배열에 자연수 x를 넣는다.
배열에서 가장 큰 값을 출력하고, 그 값을 배열에서 제거한다.
'''

import sys, heapq ; input = sys.stdin.readline
n = int(input())
heap = []

for _ in range(n):
    num = int(input())
    if num:
        heapq.heappush(heap, (-num))
    else:
        try:
            print(-1 * heapq.heappop(heap))
        except:
            print(0)