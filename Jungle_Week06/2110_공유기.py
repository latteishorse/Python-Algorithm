import sys
input = sys.stdin.readline

n,c = map(int,input().split())
house = sorted([int(input()) for _ in range(n)])
# 입력 받은 값을 오름차순으로 정렬

start = 1 # 좌표값의 최소값
end = house[-1] - house[0] # 가장 높은 좌표와 가장 낮은 좌표의 차이

result = 0

while (start <= end):
    mid = (start+end)//2 # 해당 gap
    old = house[0]
    count = 1

    for i in range(1, len(house)):
        if house[i] >= old + mid: # gap 이상
            count+=1
            old = house[i]
    
    if count < c:
        # 검색 범위를 앞으로
        end = mid - 1
    else:
        # 검색 범위를 뒤로 좁힘
        start = mid + 1
        # 지금까지의 값 저장
        result = mid

print(result)
