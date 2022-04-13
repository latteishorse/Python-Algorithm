import sys
from bisect import bisect_right, bisect_left
input = sys.stdin.readline

n = int(input())
array = list(map(int, input().split()))

array.sort()

m = int(input())
target = list(map(int, input().split()))

for x in target:
    right_index = bisect_right(array, x) # 정렬된 array에서 x가 위치하게될 오른쪽 인덱스(왼쪽값보다 크지만 오른쪽 값보다 작은 지점의 인덱스)
    # 4 1 5 2 3
    # 1
    # bisect_right(arr, 1)
    # 2
    # bisect_left(arr, 1)
    # 1
    # 

    left_index = bisect_left(array, x) # 정렬된 array에서 x가 위치하게될 왼쪽 인덱스(왼쪽값보다 크지만 오른쪽 값보다 작은 지점의 인덱스)

    if right_index > left_index: 
        # right_index와 left_index가 차이가 난다면 해당 숫자가 존재하는 것이기에 1을 출력

        print(1)
    else: 
        # right_index와 left_index가 차이가 난다면 해당 숫자가 없는 것이기에 0을 출력
        print(0)

# bisect.bisect_right(a, x, lo, hi)
#     a : 배열
#     x : 찾고자 하는 값
#     lo, hi : 배열의 범위를 지정하는 값(지정하지 않는 경우 배열 전체 탐색 <lo = 0, hi = len(a)>)
#     lo = 배열의 시작 범위
#     hi = 배열의 끝 범위