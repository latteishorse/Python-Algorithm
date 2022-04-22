# 9084
# 동전으로 금액을 만드는 모든 경우의 수

# DP
# 배낭문제
# 금액 범위 (1<= <=10000) 

# 테스트 케이스 T
# 동전의 가지 수 N
# N가지 동전의 각 금액
# 만들어야 할 금액 M
import sys
input = sys.stdin.readline

t = int(input())
for i in range(t):
    n = int(input())
    c = list(map(int, input().split()))
    m = int(input())

    dp = [0 for _ in range(m + 1)]

    dp[0] = 1
    for i in c:
        for j in range(1, m + 1):
            if j >= i:
                dp[j] += dp[j - i]
    print(dp[m])