# 1629

# A를 B번 곱한다.
# C로 나눈 나머지

# (A^B) % C

# pow(x, y, z) is equal to x**y % z

# A, B, C = map(int, input().split())
# print(pow(A,B,C))

#---

import sys
input = sys.stdin.readline

a, b, c = map(int, input().split())

def pw(a: int, b: int, c: int):
    if b == 1:
        return a % c

    if b % 2 == 0: # 짝수
        return (pw(a, b//2,c)**2) % c

    else:   # 홀수
        return (pw(a,b//2,c)**2 * a) % c

print(pw(a, b, c))