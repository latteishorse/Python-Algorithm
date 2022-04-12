# 10819
# 차이를 최대로

# backtracking으로 접근

# def dfs(depth):
#     if depth == N:
#         res.append(sum(abs(li[i+1]-li[i]) for i in range(N-1)))
#         return 
#     for i in range(N):
#         if check[i]:
#             continue
#         li.append(nums[i])
#         check[i] = 1
#         dfs(depth+1)
#         li.pop()
#         check[i] = 0

# N = int(input())
# nums = list(map(int, input().split()))
# li, res = [], []
# check = [0]*N
# dfs(0)
# print(max(res))

# permutation 방법
# 모든 방법 비교

from itertools import permutations

N = int(input())
nums = list(map(int, input().split()))
res = 0


# 모든 경우
for per in permutations(range(N),N):
    tmp = 0
    for i in range(1,N):
        tmp += abs(nums[per[i]] - nums[per[i-1]])
    res = max(res, tmp)
print(res)