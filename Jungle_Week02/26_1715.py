# 1715

# 카드 묶음
# 1, 2, 3, -- ,n
# 12 12)3 123) -- 123n-1 , +n


# sort 해서 작은 수 
# 우선순위 큐 -> 힙
# 최소 힙 이용해서 접근

# N -> 카드 팩 수
import sys, heapq
input = sys.stdin.readline

n = int(input())
heap = []

# 카드 팩 입력
# card = [list(map(int,input().split())) for _ in range(n)]

for _ in range(n):
        heapq.heappush(heap, int(input()))
# heap.sort()
# 입력 받은 카드 팩 최소힙으로 

ans = []

while heap :
    if len(heap) == 1:
        print(sum(ans))
        break

    a = heapq.heappop(heap)
    b = heapq.heappop(heap)
    ans.append(a+b)
    
    heapq.heappush(heap, a + b)
    