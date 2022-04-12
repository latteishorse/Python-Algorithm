# 2261
# 3

import sys
n = int(sys.stdin.readline())

cord = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
nc = []

for i in range(n):
    for j in range(n):
        if i == j:
            continue
        elif j == i:
            continue
        nc.append((cord[i][0] - cord[j][0])**2 + (cord[i][1] - cord[j][1])** 2)

print(min(nc))