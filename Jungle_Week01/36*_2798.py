# 2798
# 블랙잭
# https://velog.io/@jeongdopark/Algorithm-python-%EB%B0%B1%EC%A4%80-2798%EB%B2%88

# # 접근법 1. 3중 for문
# n, m = map(int, input().split())
# num = [(map(int, input().split()))]
# l = len(num)
# ans = 0
# for i in range(0, l-2):
#     for j in range(i+1, l-1):
#         for k in range(j+1, l):
#             if(num[i] + num[j] + num[k] > m):
#                 continue
#             else:
#                 ans = max(ans ,num[i] + num[j] + num[k])

# print(ans)

# 접근법 2. permutaion
from itertools import permutations

n, m = map(int, input().split())
num = list(map(int, input().split()))
ans = 0

for i in permutations(num, 3):
    if(m+1 > sum(i)):
        ans = max(ans, sum(i))
    
print(ans)