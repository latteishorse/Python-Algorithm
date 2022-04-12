# 2750

# sorted

n = int(input())
x = [None] * n

for i in range(n):
    x[i] = int(input())

x = sorted(x)
for i in range(n):
    print(x[i])

# ------
import sys
n = int(sys.stdin.readline())
b = []

for i in range(n):
    b.append(int(sys.stdin.readline()))

b.sort()
for i in b:
    print(i)