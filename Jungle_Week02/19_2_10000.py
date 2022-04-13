# 10000
# https://velog.io/@piopiop/%EB%B0%B1%EC%A4%80-10000%EC%9B%90-%EC%98%81%EC%97%AD-%ED%8C%8C%EC%9D%B4%EC%8D%AC

import sys

N = int(input())
points = []
for _ in range(N):
    x, r =list(map(int, input().split()))
    points.append(["{", x - r, 0, 0]) 
    #괄호, 좌표, 상태(이어지면 1 아니면 0), 이어진 원 지름 길이의 합  
    points.append([")", x + r, 0, 0])
points.sort(key=lambda x:(x[1], x[0])) 

stack = []
answer = 1

for i in range(len(points)):
    # 시작점일 경우
    if points[i][0] == "{":
        
        if stack:
            if stack[-1][1] == points[i][1] or stack[-1][3] == points[i][1]: 
                stack[-1][2] = 1
            else:
                stack[-1][2] = 0
        stack.append(points[i])
    else:
        half = stack.pop()
        if stack and stack[-1][2] == 1:
            stack[-1][3] = points[i][1]
        
        if half[2] == 1 and half[3] == points[i][1]:
            answer += 1
        answer += 1
print(answer)