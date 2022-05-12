# 1920
# BOJ 312ms
import sys ; input = sys.stdin.readline
from bisect import bisect_right, bisect_left

n = int(input())
arr = sorted(list(map(int, input().split())))

m = int(input())
key = list(map(int, input().split()))

for x in key:
    right_index = bisect_right(arr, x)
    left_index = bisect_left(arr, x)

    if right_index > left_index:
        print(1)
    else:
        print(0)