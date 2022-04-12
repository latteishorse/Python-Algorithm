# 2730
# 쿼드 트리 문제
import sys
input = sys.stdin.readline

n = int(input())
paper = [list(map(int,input().split())) for _ in range(n)]
result = []

def paperCutter(x,y,N):
    color = paper[x][y]
    # 2차 배열
    for i in range(x, x+N):
        for j in range(y, y+N):
            if color != paper[i][j]:
                paperCutter(x, y, N//2)
                paperCutter(x, y+(N//2), N//2)
                paperCutter(x+(N//2), y, N//2)
                paperCutter(x+(N//2), y+(N//2), N//2)
                return
    if color == 0:
        result.append(0)
    else:
        result.append(1)

paperCutter(0,0,n)
print(result.count(0))
print(result.count(1))

#     [(i,j) for i in range(x, x+N) for j in range(y,y+N) if color != paper[i][j]]

#     하얀색과 파란색을 나눠서 출력해야함
#     if 현재 섹터가 모두 true 면 분할 종료
#         if 파란색
#         현재 수 저장 -> 색 지정
#         else:
#             흰색 수 저장

#     수 + 4  
#     return 색종이 더 자르게 분할 -> 색 상관 없이

# print(흰색 종이 수)
# print(파란색 종이 수)

# 2^k * 2^ k = 4^k

# 첫 색상과 나머지 색상이 같은지 확인
# 
# import sys

# N = int(sys.stdin.readline())
# paper = [list(map(int, sys.stdin.readline().split())) for _ in range(N)] 

# result = []

# def solution(x, y, N) :
#   color = paper[x][y]
#   for i in range(x, x+N) :
#     for j in range(y, y+N) :
#       if color != paper[i][j] :
#         solution(x, y, N//2)
#         solution(x, y+N//2, N//2)
#         solution(x+N//2, y, N//2)
#         solution(x+N//2, y+N//2, N//2)
#         return
#   if color == 0 :
#     result.append(0)
#   else :
#     result.append(1)


# solution(0,0,N)
# print(result.count(0))
# print(result.count(1))

