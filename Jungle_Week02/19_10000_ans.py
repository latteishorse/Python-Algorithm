import sys
from bisect import  *
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

# 원 갯수
num = int(input())
ans =2

# 원 좌표, 반지름 입력
circles= []
for _ in range(num):
    # 중심, 반지름 각각 나눠서 입력 받음
    center , banji=  map(int,input().split())
    # 중심과 반지름 차로 원의 끝 지점 좌표 계산
    circles.append([center-banji , center +banji])

# circles 리스트에 x 좌표가 작은 순서대로 정렬
# circles.sort(key= lambda x:( x[0], -x[1]))
circles.sort(key= lambda x : x[0])

# 
def checking(start_int, end):
    # 
    if start_int == num:
        return 0
    # 다다음 원의 시작점과 끝점이 원을 채움
    # 0에서 시작해서, 2에서 끝나는 원 + 2에서 시작해서 4에서 끝나는 원이
    # 0, 4 원을 채움
    elif circles[start_int][1]==end:
        return 1

    # -----
    # 이 조건이 필요한 이유를 모르겠어서 주석처리
    # elif circles[start_int][1]!=end:

        # 배열 이진분할
        # circles에 [circles[start_int][1] 왼쪽 위치가 temp_int
        # 의미는?

        # 
        # tmp_int =bisect_left(circles,[circles[start_int][1],]) 
        
        # if circles[tmp_int][0] is not None and circles[tmp_int][0] == circles[start_int][1]:
        #     return 1* checking(tmp_int,end)
        # else:
        #     return 0

        # -----
        
    else:
        return 0

# -----
# 좌표를 이동시켜가면서 비교

for i in range(num-1):
    # 같은 지점에서 시작하는 경우
    if circles[i][0] == circles[i+1][0]:
        # 원의 시작점과 끝점이 동일할 경우 -> 동일 원일 경우
        # 이 조건은 없어도 되지 않을까?
        # if circles[i][1] == circles[i+1][1]:
        #     ans+=1
        # else:

            # 왼쪽 인덱스를 구하기
            # circle[i+1][1]은 다음 원의 y 좌표
            # 
            start_int = bisect_left(circles,[circles[i+1][1]])

            # start_int 원의 시작과 i+1원의 끝이 일치할 경우
            # 
            if circles[start_int][0] == circles[i+1][1]:

                # 접한다 -> 반지름을 모두 채우는 케이스
                if checking(start_int, circles[i][1]) ==1:
                    ans +=2

                # 접한다 -> 반지름을 모두 채우지는 않는다
                else:
                    ans +=1
            # 
            else:
                ans+=1

    # 시작점이 이어지지 않고 시작하는 경우 -> 접하지 않는다 
    else:
        ans +=1


print(ans)