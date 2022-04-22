# 11047
# 매트로이드 문제 -> 근사해 = 최적해
# n개의 동전, k원을 만들기 위해 필요한 동전 개수의 최솟값

# n, k
# from collections import deque

n, k = map(int, input().split())
coin = []
cnt = 0

for _ in range(n):
    coin.append(int(input()))

coin = sorted(coin, reverse=True)

while k != 0 :
    if k // coin[0] > 0 :
        cnt += (k//coin[0])
        k = k % coin[0] 
        coin.pop(0)
    else :
        coin.pop(0)

print(cnt)

# 숏코딩
n, k = map(int, input().split())

nl = []
for i in range(n):
    nl.append(int(input()))
    
nl.reverse()

cnt = 0
for i in nl:
    cnt += k//i
    k = k%i

print(cnt)