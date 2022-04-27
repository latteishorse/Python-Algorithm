'''
if a <= 0 or b <= 0 or c <= 0, then w(a, b, c) returns:
    1

if a > 20 or b > 20 or c > 20, then w(a, b, c) returns:
    w(20, 20, 20)

if a < b and b < c, then w(a, b, c) returns:
    w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)

otherwise it returns:
    w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)

'''
import sys
input = sys.stdin.readline

def recur(a,b,c):
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    elif a > 20 or b > 20 or c > 20:
        return recur(20, 20, 20)
    elif dp[a][b][c]:
        return dp[a][b][c]
    elif a<b<c :
        dp[a][b][c] = recur(a, b, c-1) + recur(a, b-1, c-1) - recur(a, b-1, c)
        return dp[a][b][c]
    dp[a][b][c] =  recur(a-1, b, c) + recur(a-1, b-1, c) + recur(a-1, b, c-1) - recur(a-1, b-1, c-1)
    return dp[a][b][c]

dp = [[[0]*21 for _ in range(21)] for _ in range(21)]

while True:
    a, b, c = map(int,input().split())

    if a == b == c == -1:
        break
    print(f"w({a}, {b}, {c}) =", recur(a,b,c))
