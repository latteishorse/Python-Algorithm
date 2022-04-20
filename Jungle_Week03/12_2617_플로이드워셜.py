# 2617
#https://kspsd.tistory.com/15

# 구슬을 무게 순으로 -> 가운데로 올 수 없는 구슬의 수
import sys
# from pprint import pprint
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [[0]*(N+1) for _ in range(N+1)]

# 앞 번호가 뒤 번호보다 무겁다
# M개의 쌍만큼 존재

for i in range(M):
    s, e = map(int, input().split())
    arr[s][e] = 1 # -> 
#     # arr.append
# pprint(arr)
# print('------')

# 플로이드 와샬
for k in range(1, N+1): # 거쳐가는 노드
    for i in range(1, N+1): # 출발 노드
        for j in range(1, N+1): # 도착 노드
            if i == j:        # if i == j: # 자기 자신으로 갈 경우 비용 0으로 초기화 하거나 continue 처리
                arr[i][j] = 0
            elif arr[i][k] and arr[k][j]: # 출발 - 거쳐가는 노드 and 거쳐가는 - 도착 노드
                arr[i][j] = 1
                # 플로이드 워셜을 쓰는 이유
                # 모든 노드를 이어보면서 이어질 수 있는 것을 이어서 테이블에 배치

# pprint(arr)

ans = 0

# i가 j보다 무겁다
# 같은 i일때 = 같은 번호일때 (특정 번호일때)
# j값이 있다면 
# i > j 이기 때문에 현재 구슬보다 가벼운거 


# 반대로 j값이 같다면
# j값 보다 i 값이 무거운거 판단

for i in range(1, N+1):
    left_cnt = 0
    right_cnt = 0

    for j in range(1, N+1):
        if arr[i][j] == 1: # 현재 구슬보다 가벼운 갯수 세기
            right_cnt += 1
            # print('i :', i,'j :',j,'r')
            # print(right_cnt, 'r count')

        elif arr[j][i] == 1:# 현재 구슬 보다 무거운 갯수 세기
            left_cnt += 1
            # print('j :', j,'i :',i,'l')
            # print(left_cnt, 'l count')

    if right_cnt > N//2 or left_cnt > N//2: # 가볍거나 무거운 개수가 중간값 보다 많으면 될 수가 없다
        # 얼마나 중앙에서 치우쳐져 있는지를 판단한다는 뜻

        ans += 1

print(ans)