import sys, heapq
input = sys.stdin.readline

n = int(input())
heap = []

for _ in range(n):
    num = int(input())
    if num != 0:
        # 가장 작은 원소를 heappop이 출력하기 때문에
        # 이를 이용하여 - 값을 저장
        heapq.heappush(heap, (-num))
    else:
        try:
            print(-1 * heapq.heappop(heap))
        except:
            print(0)