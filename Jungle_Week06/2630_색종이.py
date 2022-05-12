import sys; input = sys.stdin.readline

n = int(input())
paper = [list(map(int, input().split())) for _ in range(n)]
result = []

def paperCutter(x,y,N):
    color = paper[x][y]
    for i in range(x, x+N):
        for j in range(y, y+N):
            if color != paper[i][j]: 
                paperCutter(x,y,N//2)
                paperCutter(x,y+(N//2),N//2)
                paperCutter(x+(N//2),y,N//2)
                paperCutter(x+(N//2),y+(N//2),N//2)
                return
    if color == 0:
        result.append(0)
    else:
        result.append(1)

paperCutter(0,0,n)
print(result.count(0))
print(result.count(1))
