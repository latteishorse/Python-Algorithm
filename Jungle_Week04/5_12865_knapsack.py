# 12865
# 01 knapsack problem

# 여행에 가져갈 물건 N개
# 각 물건 무게: W, 가치: V
# 해당 물건을 넣어가면 V 만큼 즐길 수 있다

# 최대 K만큼 무게만 가져갈 수 있음
# 넣을 수 있는 물건들의 가치의 최댓값

# N, K

# W V - N개의 줄
'''
① j < weight : d[i][j] = d[i-1][j]
② d[i][j] = max( d[i-1][ j-weight ]+value ), d[i-1][j] )
'''
import sys
input = sys.stdin.readline

n, k = map(int, input().split())

thing = [[0,0]]
d = [[0]*(k+1) for _ in range(n+1)]

for i in range(n):
    thing.append(list(map(int, input().split())))

for i in range(1, n+1):
    for j in range(1, k+1):
        w = thing[i][0]
        v = thing[i][1]

        if j < w:
            d[i][j] = d[i-1][j]
        else:
            d[i][j] = max(d[i-1][j], d[i-1][j-w]+v)

print(d[-1][-1])