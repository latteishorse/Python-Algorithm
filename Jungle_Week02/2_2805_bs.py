# Parametric Search
# 최적화 문제를 결정 문제로 바꾸어 해결하는 기법
# 파라메트릭 서치 문제는 이진 탐색을 재귀적으로 구현하지 않고 반복문으로 구현하면 더 간결

# 나무 수, 나무 길이
n, m = list(map(int, input().split()))
# 나무 높이
array = list(map(int, input().split()))

# 시작점과 끝점
start = 0
end = max(array)

# 이진 탐색
result = 0
while(start <= end):
    
    total = 0
    mid = (start + end) // 2

    for x in array:
        if x > mid:
            total += x - mid
            
    if total < m:
        end = mid - 1
    else:
        result = mid
        start = mid + 1

print(result)