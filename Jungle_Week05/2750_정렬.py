# 2750
import sys; input = sys.stdin.readline
n = int(input())

num = []
for _ in range(n):
    num.append(int(input()))

num = sorted(set(num))
print(*num, sep ='\n')