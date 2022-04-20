# 2294


# 목표치 K원

# 1 * i 
# 2 * j
# 3 * k

# i + j + k = 15

#d[k] -> 경우의 수를 저장
# d[k] = d[k] + d[k-coin[n]]

# n, k = map(int, input().split())
# coin = [int(input()) for _ in range(n)] # 코인의 종류
# dp = [0 for _ in range(k+1)] # 사이즈 k+1만큼의 리스트 선언
# dp[0] = 1 # 인덱스 0은 동전을 1개만 쓸 때의 경우의 수를 고려하기 위해 선언

# for i in coin:
#     for j in range(i, k+1):
#         if j-i >= 0:
#             dp[j] += dp[j-i]

# print(dp[k])

# bfs

# 카운트 1부터
# 순차적으로 하나씩 더해보면서 
# 원하는 값이 될때 종료

import sys
input = sys.stdin.readline
from collections import deque

n, k = map(int, input().split())
coins=list(set(int(input()) for _ in range(n)))

visited = [False for _ in range(k+1)] 
queue=deque()

def bfs(coins, k):
    for coin in coins:
        if coin < k:
            queue.append([coin,1])
            visited[coin] = True

    while queue:
        coinSum, count = queue.popleft()

        if coinSum == k:
            print(count)
            break

        for coin in coins:
            updateSum = coinSum+coin
            updateCount = count + 1

            if updateSum > k:
                continue

            elif updateSum <= k and not visited[updateSum]:

                visited[updateSum] = True
                queue.append([updateSum,updateCount])
            
    if coinSum != k:
        print(-1)
bfs(coins,k)

# ---
import sys
from collections import deque
read=sys.stdin.readline
n,k = map(int,read().split())
# set로 받는 이유는 같은 coin이 들어올 수 있기 때문
coins = list(i for i in set(int(read()) for _ in range(n)) if i <=k)
if k in coins:
    print(1)
    exit()
# deque([(0, 1), (1, 5), (2, 12)])
que = deque([(i, coin) for i, coin in enumerate(coins)])
visit = [0]* (k + 1)
for i in coins:
    visit[i] = 1
cnt = 1
while que:
    for _ in range(len(que)):
        index, coin_sum = que.popleft()
        # 왜 시작이 index냐면 5,12 더하는 것과 12,5 더하는 건 같기 때문. 5면 5, 12 더하고 12 면 12만 해주면됨
        # 소수 찾기에서 2*3 이랑 3*2랑 중복되는 부분 피해주는거랑 비슷한 개념
        for i in range(index, len(coins)):
            new_sum = coin_sum + coins[i]
            if new_sum == k:
                print(cnt + 1)
                exit(0)
            if new_sum <= k and not visit[new_sum]:
                que.append((i, new_sum))
                visit[new_sum] = 1
    cnt +=1
print(-1)
