# 2750
import sys; input = sys.stdin.readline
n = int(input())

num = []
[num.append(int(input())) for _ in range(n)]

num.sort()
print(*num, sep ='\n')