# 2798

from itertools import permutations

n, goal = map(int, input().split())
nums = map(int, input().split())

black = 0
for i in permutations(nums, 3):
    if sum(i) <= goal:
        black = max(black, sum(i))

print(black)