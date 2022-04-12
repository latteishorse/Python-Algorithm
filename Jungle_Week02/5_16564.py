# 16564

# 이분 탐색 이외 접근 시도

# n, t = map(int, input().split())
# lv = []
# for _ in range(n):
#     lv.append(int(input()))

# lv.sort()

# while t != 0:
#     if lv[0] < lv[1]:
#         lv[0] += 1
#         t -= 1

#     elif lv[0] == lv[1]:
#         lv[0] += 1
#         t -= 1
#         lv[1] += 1
#         t -= 1
    
#     if t == 0:
#         break

# print(lv[0])

# -----
# 이분 탐색
# import sys
# input = sys.stdin.readline

# N, K = map(int, input().split())
# lv = sorted([int(input()) for _ in range(N)])

# left, right = min(lv), max(lv)+K
# ans = 0

# def count(lv, mid):
#     t = 0
#     for i in lv:
#         if i >= mid:
#             break
#         t += mid - i
#     return t

# while left < right:
#     mid = (left+right)//2

#     if count(lv, mid) <= K:
#         ans = mid
#         left = mid + 1
#     else:
#         right = mid - 1

# print(ans)

# -----

import sys
input = sys.stdin.readline

N, K = map(int, input().split())
lv = []
for i in range(N):
    lv.append(int(input()))

lv.sort()

left, right = min(lv), max(lv)+K
ans = 0

def count(lv, mid):
    t = 0
    for i in lv:
        if i >= mid:
            break
        t += mid - i
    return t

while left <= right:
    mid = (left+right)//2
    if count(lv, mid) <= K:
        ans = mid
        left = mid + 1
    else:
        right = mid - 1

print(ans)