# 15649

# 3. 재귀함수를 이용하여 m개의 수열을 저장하기 위한 리스트
# 6. 리스트에 들어간 수열들이 m개가 되면 리스트에 들어있는 숫자들을 모두 출력하고 함수를 나온다.
# 10. for문을 이용하여 1부터 n까지의 숫자들을 모두 확인
# 11. 리스트 s 중복여부 확인
# 12. 중복이 아니면 숫자 i를 리스트 s에 넣기
# 13. 현재 s=[1]인 상태에서 다음숫자를 넣기위하여 가지치기하기(재귀함수)
#   -> 만약 n=4, m=2라면 밑과 같은 형태로 진행될 것이다.
#       s : [1] -> [1,2] -> [1] -> [1,3] -> [1] -> [1,4]
#                   출력   pop(2)  출력   pop(3)  출력

# -> 런타임 뜸
# n,m = list(map(int,input().split()))
# s = []
# def dfs():
#     if len(s)==m:
#         print(' '.join(map(str,s)))
#         return
    
#     for i in range(1,n+1):
#         if i not in s:
#             s.append(i)
#             dfs()
#             s.pop()
# dfs()

# ----- > 런타임
# https://wlstyql.tistory.com/56 

# import sys
# sys.setrecursionlimit(2500)

# N, M = map(int, input().split())
# visited = [False] * N  # 탐사 여부 check
# out = []  # 출력 내용

# def dfs(depth, N, M):
#     if depth == M:  # 탈출 조건
#         print(' '.join(map(str, out)))  # list를 str으로 합쳐 출력
#         return
#     for i in range(N):  # 탐사 check 하면서
#         if not visited[i]:  # 탐사 안했다면
#             visited[i] = True  # 탐사 시작(중복 제거)
#             out.append(i+1)  # 탐사 내용
#             dfs(depth+1, N, M)  # 깊이 우선 탐색

#             # return 하면 여기로 이동
#             visited[i] = False  # 깊이 탐사 완료
#             out.pop()  # 탐사 내용 제거

# dfs(0, N, M)

# ----

def dfs():
    if len(depth) == M:
        print(' '.join(map(str,depth)))
        return
    for i in range(1, N+1):
        if i in depth: # 가지치기, 이미 선택한 숫자 배제
            continue
        depth.append(i)
        dfs() #함수호출
        depth.pop() # 출력 후 return하고 마지막 원소 비우기

N, M = map(int, input().split())
depth = []
dfs()

