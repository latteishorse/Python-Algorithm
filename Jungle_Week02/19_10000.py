from turtle import circle


n = int(input())

# 이중 배열로 입력 받고,
crc = [list(map(int,input().split())) for _ in range(n)]
ncr = []
# 배열을 sort 시킴 → 어떻게 크기별로 배치시킬 수 있을까?
# x좌표 - 반지름 값이 가장 작은 순서대로 배치하는게 맞을듯
# 리스트 내 값을 연산해서 배치할 수 있을까?

# for _ in range(n):
ncr = sorted(crc[0] - crc[1])

crc.sort()
print(crc)

# 

# 해당 순서대로 배치 후

# 반은 순서대로 원 전개 → 그려봄

# // 우선 스택 쓰지말고 입력 받은 x-r 좌표 sort 해보자

# 1. x-r 좌표 리스트와 x+r 좌료 리스트에서 공통된 좌표 찾기
# 2. 해당 위치에서 생성되는 두 원의 반지름이 다른 원 하나의 반지름을 만족하는지 확인하기
# - 만족한다 +2
# - 만족하지 않는다 + 1

# -----