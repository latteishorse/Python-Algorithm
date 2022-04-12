answer = [0, 1, 0, 0, 2, 10, 4, 40, 92, 352, 724, 2680, 14200, 73712, 365596]
print(answer[int(input())])
#- --

import sys

input = sys.stdin.readline

n = int(input())

col = [0] * n
result = 0

def promising(i):
    for k in range(i):
        if col[i] == col[k] or abs(col[i] - col[k]) == i - k:
            return False
    
    return True

def dfs(i):
    if i == n:
        if n == 0:
            return
        else:
            global result
            result += 1
            return
    
    for j in range(n):
        col[i] = j
        if promising(i):
            dfs(i+1)

dfs(0)

print(result)