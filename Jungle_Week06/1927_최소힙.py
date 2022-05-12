# 1927
'''
배열에 자연수 x를 넣는다.
배열에서 가장 작은 값을 출력하고, 그 값을 배열에서 제거한다.
'''
import sys ; input = sys.stdin.readline
from heapq import heappush, heappop

n = int(input())
heap = []

for _ in range(n):
    num = int(input())
    if num:
        heappush(heap, num)
    else:
        try:
            print(heappop(heap))
        except:
            print(0)
