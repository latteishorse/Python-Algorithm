# 5568

# 아이디어
# nPr -> 순열로 풀어야 순서를 고려
# set으로 중복 제거

from itertools import permutations
import sys
input = sys.stdin.readline

n = int(input())
k = int(input())
b = []

for _ in range(n):
    b.append(input().strip())

result = set()
for i in permutations(b, k):
    result.add(''.join(i))

print(len(result))

# 백트래킹
# def dfs(depth):
#     if depth == k:
#         s.add(''.join(map(str, li)))
#         return
#     for i in range(n):
#         if check[i]:
#             continue
#         li.append(nums[i])
#         check[i] = 1
#         dfs(depth+1)
#         li.pop()
#         check[i] = 0
        
# n, k = int(input()), int(input())
# nums = [int(input()) for _ in range(n)]
# li, s = [], set()
# check = [0]*n
# dfs(0)
# print(len(s))