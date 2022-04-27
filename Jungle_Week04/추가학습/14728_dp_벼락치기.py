# 14728

# 넣을 수 있는 수 / 가치
n, k = map(int, input().split())

test = [[0,0]]
d = [[0]*(k+1) for _ in range(n+1)]

for _ in range(n):
    test.append(list(map(int, input().split())))

for i in range(1, n+1):
    for j in range(1, k+1):
        time = test[i][0]
        score = test[i][1]

        if j < time:
            d[i][j] = d[i-1][j]
        else:
            d[i][j] = max(d[i-1][j], d[i-1][j-time] + score)

print(d[-1][-1])

# ---
# https://www.acmicpc.net/source/42470915
n, t = map(int, input().split())

data = []
for i in range(n):
    a, b = map(int, input().split())
    data.append((a,b))

data.sort()

dp = [0] * (t+1)
for i in range(1, t+1):
    if i >= data[0][0]:
        dp[i] = data[0][1]


for i in range(1, n):
    for j in range(t, data[i][0]-1, -1):
        dp[j] = max(dp[j], dp[j-data[i][0]]+data[i][1])

print(dp[-1])