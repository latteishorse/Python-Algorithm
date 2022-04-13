import sys
input = sys.stdin.readline

k, n = map(int, input().split())

array = [int(input()) for _ in range(k)]

left = 1
right = max(array)

while left <= right:
        cnt = 0
        mid = (left + right) // 2

        for x in array:
            cnt += x // mid
        if cnt >= n:
            left = mid + 1
        else:
            right = mid - 1

print(right)
# 1654
import sys
input = sys.stdin.readline

k, n = map(int, input().split())

array = [int(input()) for _ in range(k)]

left = 1
right = max(array)

while left <= right:
        cnt = 0
        mid = (left + right) // 2

        for x in array:
            cnt += x // mid
        if cnt >= n:
            left = mid + 1
        else:
            right = mid - 1

print(right)