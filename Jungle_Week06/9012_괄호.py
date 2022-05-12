# 9012
import sys; input = sys.stdin.readline

N = int(input())

for _ in range(N):
    score = 0
    bracket = list(input())
    for i in bracket:
        if i == '(':
            score += 1
        elif i == ')':
            score -= 1

        if score < 0:
            print('NO')
            break

    if score > 0:
        print('NO')
    elif not score:
        print('YES')
