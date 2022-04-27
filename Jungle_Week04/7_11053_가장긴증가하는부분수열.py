# 11053

# 항상 증가해야 하므로
# 스택으로 하나씩 넣고, pop 시켜보면서 확인해야할듯

# from collections import deque
# n = int(input())
# queue = deque()

# nums = list(map(int, input().split()))

# # dp - O(N^2)
# N = int(input())
# A = list(map(int, input().split()))

# dp = [1] * N

# for i in range(N):
#     for j in range(i):
#         if A[j] < A[i]:
#             dp[i] = max(dp[i],dp[j]+1)

# print(max(dp))

# binary search
# O(N logN)

import bisect

x = int(input())
arr = list(map(int, input().split()))

#1. dp를 arr[0]으로 초기화한다.
dp = [arr[0]]

for i in range(x):
    #2. 현재 위치(i)가 이전 위치의 원소들보다 크면 dp에 추가한다.
    if arr[i] > dp[-1]:
        dp.append(arr[i])
    else:
        #3. 현재 위치(i)가 이전 위치의 원소보다 작거나 같으면, 
        # bisect.bisect_left로 이전 위치의 원소 중 가장 큰 원소의 index값을 구한다. 
        # 그리고 dp의 index 원소를 arr[i]로 바꿔준다.
        idx = bisect.bisect_left(dp, arr[i])
        dp[idx] = arr[i]

print(len(dp))

