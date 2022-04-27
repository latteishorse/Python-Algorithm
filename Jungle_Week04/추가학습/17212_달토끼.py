# 17212

# 1,2,5,7
# N원

n = int(input())
# coin = [7,5,2,1]
coin = [1,2,5,7]

dp = [100001] * (n+1)
dp[0] = 0

for i in coin:
    for j in range(i, n+1):
        # 
        if  dp[j] >= dp[j-i]+1:
            dp[j] = dp[j-i]+1
            print(dp)

print(dp[-1])


# coin = sorted(coin, reverse=True)
# cnt = 0
# while k != 0 :
#     if k // coin[0] > 0 :
#         cnt += (k//coin[0])
#         k = k % coin[0] 
#         coin.pop(0)
#     else :
#         coin.pop(0)

# print(cnt)

