# 10989
import sys; input = sys.stdin.readline
n = int(input())
indexArr = [0] * 10001
for _ in range(n):
    nums = int(input())
    indexArr[nums] += 1

for i in range(10001):
    if indexArr[i] != 0:
        for _ in range(indexArr[i]):
            print(i)
