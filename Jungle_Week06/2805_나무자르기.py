#2805
'''
나무의 남은 부분 만큼만 가져가도록 해야함
M 이상 가져갈 수 있도록

첫 입력
나무 수 N , 가져가려는 나무 길이 M

둘째 줄에는 나무의 높이 -> 한줄로 주어짐

완전 탐색하면 시간에 걸림
'''
# 완전탐색 -> 시간초과
import sys; input = sys.stdin.readline

n, m = map(int, input().split())
height = list(map(int, input().split()))

for i in range(max(height)-1,0,-1):
    tree = 0
    for x in height:
        branch = x - i
        if branch > 0 :
            tree = tree + branch
        if tree >= m:
            print(i)
            exit(0)

# ------

# 이진탐색
#2805
import sys; input = sys.stdin.readline

n, m = list(map(int, input().split()))
height = list(map(int, input().split()))

start = 0; end = max(height); result = 0

while(start <= end):
    total = 0
    mid = (start + end) // 2

    for x in height:
        if x > mid:
            total += x - mid
    if total < m:
        end = mid - 1
    else:
        result = mid
        start = mid + 1

print(result)