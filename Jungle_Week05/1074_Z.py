# 1074
import sys ; input = sys.stdin.readline
n, r, c = map(int, input().split())

def zSolver(n,r,c):
    if n == 0:
        return 0
    return (c%2) + 2*(r%2) + 4*zSolver(n-1,int(r/2),int(c/2))

print(zSolver(n,r,c))