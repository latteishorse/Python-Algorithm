# 13334

# 문제 접근
# 제한 사항
# 철로의 길이 d

# 아이디어
# 1. 모든 좌표를 힙에 넣음
# 2. 최소힙에서 공통되는 부분을 체크 -> 어떻게?




# n 명의 사람

#----------------------------

# import heapq, sys
# input = sys.stdin.readline

# n = int(input())
# heap = []
# for _ in range(n):
#         heapq.heappush(heap, list(map(int, input().split())))

# https://github.com/emplam27/Python-Algorithm/blob/master/%EB%B0%B1%EC%A4%80/%EB%B0%B1%EC%A4%80_13334_%EC%B2%A0%EB%A1%9C.py

# import sys
from heapq import heappush, heappop
import sys

# sys.stdin = open('input.txt', 'r')
read = sys.stdin.readline

'''
모든 좌표들을 (작은좌표(A), 큰좌표(B)) 순서대로 바꿔준 뒤 정렬한다. 정렬할때 큰좌표(B) 기준으로 정렬한다.
이후 is_possible을 만들어 준다.
is_possible은 최소힙. rails의 A부터 A + D 사이에 들어오는 location들이 저장한다.
rails에서 차례대로 순회하면서 is_possible에 push한다. 
만일 is_possible의 루트노드가 A 부터 A + D 범위에서 벗어난다면 pop 해준다.
'''

N = int(read())
locations = [list(map(int, read().split())) for _ in range(N)]
D = int(read())

# (집 좌표, 사무실 좌표)를 앞쪽에 항상 작은 좌표가 오도록 바꿔줌
for location in locations:
    if location[0] > location[1]:
        location[0], location[1] = location[1], location[0]
locations.sort(key=lambda x: x[1])

is_possible = []
index, result = 0, 0
for location in locations:
    # 범위를 설정
    start, end = location[1] - D, location[1]

    # 범위를 벗어난 location이라면 넘어감
    if location[1] - location[0] > D:
        continue

    # 범위 안에 들어오는 경우 push
    if start <= location[0] and location[1] <= end:
        heappush(is_possible, location)

        # 범위를 벗어나는 값이 생기면 pop
        while is_possible[0][0] < start:
            heappop(is_possible)
    result = max(result, len(is_possible))

print(result)