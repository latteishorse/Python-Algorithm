# 

import sys
input = sys.stdin.readline

m, n, l = map(int,input().split())
lane = sorted(list(map(int, input().split())))
# ani = []
# for _ in range(n):
#     ani.append(map(int, input().split()))

ani = [list(map(int, input().split())) for _ in range(n)]

cnt = 0
for a, b in ani:
# 시작점과 끝점
    start = 0
    end = len(lane) -1

# 이진 탐색
    while start < end :
        #
        mid = (start + end) // 2

        if lane[mid] < a:
            start = mid + 1
        else:
            end = mid - 1

# ######
#     if abs(lane[end]-a) + b <=1 or abs(lane[end-1]-a) + b <= 1:
#         cnt += 1

print(cnt)




# for i in range():
#     if ani[i][-1]


# 사로를 먼저 정한다
# 사로에서 사정거리를 확인한다
# 사정거리 내에 동물을 카운트한다

# 삼각형으로 접근
# (l, xg)
# (xg-l,0) ~ (xg+l,0)
# (xg-l+y,y), (xg+l-y,y)

# for i in ():
    
#     if 동물 좌표 > xg-l+y and 동물 y좌표 < Y
#         if 동물 x < xg + l - y and 동물 y < y

# ---------
y <= l and xg-l <= x <= xg + l) and (x - (xg-l) >= y and x - xg + y <= l
