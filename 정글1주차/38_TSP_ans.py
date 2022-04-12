import sys
from itertools import permutations
input = sys.stdin.readline

# 도시 수
n = int(input())

# # 도시 이동 비용
# cost =[]
# for _ in range(n):
#     cost.append(list(map(int, input().split())))

cost = [list(map(int, input().split())) for _ in range(n)]

# 도시 이동 비용 완전탐색
def function(k):
    ans = 0

    # 앞 도시부터 순서대로 노드 연결
    for i in range(n-1):
        if cost[k[i]] and cost[k[i+1]] != 0:

            # i 번째 리스트 중 i+1 인덱스를 꺼낸다
            ans += cost[k[i]][k[i+1]]
        #     
        else:
            return False
    # 0일 경우 = 자기 도시로 갈 경우
    # 맨 뒤 도시 중 첫 번째
    if cost[k[-1]][k[0]] == 0:
        return False
    # 다른 도시로 이동하도록
    else:
        ans += cost[k[-1]][k[0]]
    return ans

# 한계값
ans = int(1e9)

# permutation 사용해서 모든 경우의 수 탐색
for k in permutations(range(n),n):
    result = function(k)
    if result != False:
        # 새로 탐색한 경우에서 최소값이 발견되면 해당 값을 ans에 저장
        ans = min(ans, result)

print(ans)

# ---
# boj 제출 코드

import sys
from itertools import permutations
input = sys.stdin.readline

n = int(input())
data = [list(map(int,input().split())) for _ in range(n)]

def function(List):
    ans = 0
    for i in range(n-1):
        if data[List[i]][List[i+1]] != 0:
            ans += data[List[i]][List[i+1]]
        else:
            return False
        
    if data[List[-1]][List[0]] == 0:
        return False
    else:
        ans += data[List[-1]][List[0]]
    
    return ans

ans = 987654321
for List in permutations(range(n),n):
    result = function(List)
    if result != False:
        if ans > result:
            ans = result
print(ans)