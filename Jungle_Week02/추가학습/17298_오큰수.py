import sys 
input = sys.stdin.readline

n = int(input()) 
nge = list(map(int, input().split())) 
stack = []
ans = [-1] * n

for i in range(n):
    while stack and nge[stack[-1]] < nge[i]:
            ans[stack.pop()] = nge[i]
    stack.append(i)

print(' '.join(map(str,ans)))