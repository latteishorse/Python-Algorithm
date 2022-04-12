import sys
from itertools import combinations
input = sys.stdin.readline

n, m = map(int, input().split())
nums = list(map(int, input().split()))
ans = 0

for i in range(1, n+1):
    for j in combinations(nums, i):
        if m == sum(j):
            ans += 1
        
print(ans)
