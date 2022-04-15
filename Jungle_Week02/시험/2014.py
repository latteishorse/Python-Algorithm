# 2014

# 자기 자신을 포함한 모든 곱을 판단해야됨
# 

# 우선순위 큐를 어떻게 이용할 것인가?
# -> 최소 힙으로 정렬 유지하면서
# 기존 리스트 안에서 곱해서 최소힙에 넣어주면 될 듯 ?

# import sys, heapq
# input = sys.stdin.readline
# heap = []
# # 첫째줄 K, N이 주어진다
# # 다음 줄에는 K개의 소수가 오름차순으로

# K, N = map(int, input().split())

# pri = [list(map(int, input().split()))]

# print(pri)
# print(pri[0][0], pri[0][1], pri[0][2])

# # 소수의 곱을 어떻게 표현할 것인가?


# mul = []
# for i in range(K):
#     for j in range(K):
#         mul.append(pri[0][i] * pri[0][j])


# print(mul)
# heapq.heappush

# heapq.heappush()


# ------
# # 2075
# -> 첫 접근 - 실패
# import sys, heapq
# input = sys.stdin.readline

# n = int(input())
# heap = []

# N = [list(map(int, input().split())) for _ in range(n)]

# for i in range(n):
#     N[i].sort(reverse=True)

# for j in range(n):
#         heapq.heappush(heap, - N[j][0])

# print(-heap[n-1])

# # --
# import heapq

# n=int(input())
# graph=[]
# for i in range(n):
#   graph.append(list(map(int, input().split())))

# heap=[]
# heapq.heapify(heap)
# for i in range(n):
#   for j in range(n):
#     heapq.heappush(heap,graph[i][j])
#     if len(heap)>n:
#       heapq.heappop(heap)

# print(heapq.heappop(heap))

# -- 
# 2014
# 오답
import heapq, sys
input = sys.stdin.readline

N, K = map(int, (input().split()))

heap = []
nums = list(map(int, input().split()))

cnt = 0

# K개 만큼만 곱을 만들어 heap에 넣어둬 메모리 최소화하고자 함
while cnt < K:
    if not heap:
        for num in nums:
            heapq.heappush(heap,num)
    # O(N**2)로 접근한거 부터 잘못한듯 싶습니다.
    for i in range(N):
        for j in range(N):
            # 곱셈 구현 잘못됨
            heapq.heappush(heap, nums[i] * nums[j])
            heapq.heappush(heap, heap[i] * nums[j])
            heapq.heappush(heap, heap[i] * heap[j])

            cnt += 3

# heap 쓰면서 정렬 사용하면 안될텐데 구현 잘못됨
heap = sorted(list(set(heap)))
# 오답 출력
# 곱셈 부분에서 누락되는 값들이 있음
print(heap[K])

