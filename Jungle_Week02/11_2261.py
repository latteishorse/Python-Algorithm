# 2261
#---
# 시간 초과되지만 정답은 나오는 코드
import sys
input = sys.stdin.readlines
n = int(input())

cord = [list(map(int,input().split())) for _ in range(n)]
nc = []

for i in range(n):
    for j in range(n):
        nc.append((cord[i][0] - cord[j][0])**2 + (cord[i][1] - cord[j][1])** 2)


remove_set = {0}
li = [i for i in nc if i not in remove_set]
print(min(li))
# -----
import sys
input = sys.stdin.readline

n = int(input())

cord = [list(map(int,input().split())) for _ in range(n)]
nc = []

# o(log n) -> 잘못 접근
# def length(x,y):
#     for i in range(n):
#         for j in range(n):
#             if cord[i][0] == cord[j][0] and cord[i][1] == cord[j][1]:
#                 return
#             else :
#                 nc.append((cord[i][0] - cord[j][0])**2 + (cord[i][1] - cord[j][1])** 2)

# # o(n^2) -> 시간 초과
# for i in range(n):
#     for j in range(n):
#         nc.append((cord[i][0] - cord[j][0])**2 + (cord[i][1] - cord[j][1])** 2)


# 좌표 값 계산 먼저
ncx = []

for i in range(n):
    for j in range(n):
        ncx.append(abs((cord[i][0] - cord[j][0]) - (cord[i][1] - cord[j][1])))


remove_set = {0}
lix = [i for i in ncx if i not in remove_set]

# 가장 작은 경우만 계산


print(min(lix)**2)

# remove_set = {0}
# li = [i for i in nc if i not in remove_set]

# print(min(li))