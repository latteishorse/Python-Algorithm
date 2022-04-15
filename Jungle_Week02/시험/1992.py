# 1992

# 주어진 결과 모두 0 -> 0
# 모두 1 -> 1

# 0과 1이 섞여있으면 왼쪽 위, 오른쪽 위, 왼쪽 아래, 오른쪽 아래
# 4개의 영상을 나누어 압축
# 압축한 결과를 차례대로 괄호 안에 묶음

# 4개로 분할

# 
# 1992
import sys
input = sys.stdin.readline

n = int(input())
video = [list(map(int, input().strip())) for _ in range(n)]
result = []

def quadTree(x,y,N):
    pixel = video[x][y]
    
    for i in range(x, x+N):
        for j in range(y, y+N):
            if pixel != video[i][j]:

                result.append('(')

                quadTree(x, y, N//2)
                quadTree(x, y+(N//2), N//2)
                quadTree(x+(N//2), y, N//2)
                quadTree(x+(N//2), y+(N//2), N//2)

                result.append(')')
                return
      
    if pixel == 0:
        result.append(0)
    else :
        result.append(1)

quadTree(0,0,n)
print(''.join(map(str, result)))
