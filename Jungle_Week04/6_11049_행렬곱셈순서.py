# 11049

'''
N x M

행렬의 수 
3 -> 2가지
4 -> 3*2가지
5 -> 4*3*2가지
n -> (n-1)!

499! 너무 크므로 dp로 풀어야한다

---
한 단계씩 줄여가면서 루프를 돌아보자


'''
import sys
 
N=int(input())
matrix=[list(map(int,sys.stdin.readline().split())) for _ in range(N)]

dp=[[0]*N for _ in range(N)]

for x in range(1,N):#거리가 x인 것까지
    for i in range(N-x):#i부터 시작
        j=i+x
        dp[i][j]= sys.maxsize
        for k in range(i,j):
            dp[i][j]=min(dp[i][j], dp[i][k]+dp[k+1][j]+matrix[i][0]*matrix[k][1]*matrix[j][1])
 
 
print(dp[0][N-1])