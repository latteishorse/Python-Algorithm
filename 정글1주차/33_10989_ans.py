import sys

n = int(sys.stdin.readline())
b = []

for i in range(n):
    b[int(sys.stdin.readline())] += 1

for i in range(10001):
    if b[i] != 0:
        for _ in range(b[i]):
            print(i)
