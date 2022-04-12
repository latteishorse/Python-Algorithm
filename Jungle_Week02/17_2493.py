# 2493
# 17608 문제와 유사한 느낌
# n = int(input())
# li = list(int(input()) for _ in range(n))

# Max = li[-1]

# for i in range(n-1, -1,-1):
#     if li[i] > Max:
#         Max = li[i]

# print(Max)

# 뒤부터 하니씩 pop 시키면서 비교하면 될듯
# index 번호도 받아와야함

import sys 
input = sys.stdin.readline

n = int(input()) 
tower = list(map(int, input().split())) 
stack = [] 
ans = [0] * n 

for i in range(n):
    while stack and tower[stack[-1]] < tower[i]: 
        stack.pop() 
    if stack: 
        ans[i] = stack[-1] + 1
    stack.append(i) 

print(' '.join(map(str,ans)))
