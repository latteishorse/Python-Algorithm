# 1655
# 1. 시간 초과
import sys, heapq
input = sys.stdin.readline

n = int(input())
heap = []
for _ in range(n):
    heapq.heappush(heap, int(input()))
    heap.sort()
    if len(heap) % 2 == 0:
        print(heap[len(heap)//2 -1])
    else:
        print(heap[len(heap)//2])

# ----
# 2. using heap
# 중앙값을 기준으로 왼쪽, 오른쪽 나눠서 저장

import heapq
import sys

input = sys.stdin.readline

n = int(input())
left_heap = []
right_heap = []

for i in range(n):
    x = int(input())
    
    # 최대 힙
    # 최대값이 항상 위로 오도록 ->
    # 왼쪽 힙 첫번째 요소는 항상 중앙값

    # if len(left_heap) == len(right_heap):
    #     heapq.heappush(left_heap, -x)

    if i % 2 == 1:
        heapq.heappush(left_heap, -x)        
    
    # 최소 힙
    else:
        heapq.heappush(right_heap, x)
        
    # 최대 힙의 값이, 최소 힙의 값보다 커야함
    # if left_heap and right_heap and left_heap[0] * -1 > right_heap[0]:
    if left_heap and right_heap and left_heap[0] * -1 > right_heap[0]:
        
        heapq.heappush(left_heap, -heapq.heappop(right_heap))
        heapq.heappush(right_heap, -heapq.heappop(left_heap))

    print(-left_heap[0])