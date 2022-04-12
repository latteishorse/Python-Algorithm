import sys
from itertools import permutations
input = sys.stdin.readline

n = int(input())
data =[]

for _ in range(n):
    data.append(list(map(int, input().split())))

# 
def function(k):
    ans = 0

    for i in range(n-1):

        if data[k[i]] and data[k[i+1]] != 0:
#       data[1[1][1[2]]

            ans += data[k[i]][k[i+1]]
        else:
            return False
        
    if data[k[-1]][k[0]] == 0:
        return False
    else:
        ans += data[k[-1]][k[0]]
    
    return ans

ans = 987654321

# 순열을 통한 모든 경우 탐색
for k in permutations(range(n),n):
    result = function(k)
    if result != False:
        if ans > result:
            ans = result
print(ans)

# ----

# 완전 탐색 + N-queen 재귀
import sys 
def move(now, depth):  #이는 깊이 우선 탐색이라는 dfs 기법이다.
    global charge, ans 	
    #n == depth는 섬의 개수만큼 충분히 가지수를 챙겼을때 라는 조건.
    if depth == n:			  #재귀 특성상 이 재귀가 멈추기위한 조건이 제일 앞에 있다. 
        # if path[now][0] > 0:  #path는 아래 정의되어있다. 각 입력 줄이 하나의 리스트로,
        if now != 0:
        					  #입력받은 순서대로 들어가있는 리스트.
                              #path[now][0]은 1번 섬으로 돌아가는 비용이 0이 아닐경우
                              #즉 1번 섬이 가장 마지막에 오지 않았나 체크함.
            ans = min(ans, charge + path[now][0])
        return 

    visit[now] = 1		#현재/ now 
    for l in link[now]:      #link[now] = path의 비용중 0이 아닌 것들의 인덱스
        if not visit[l]:     #visit[l]의 element가 false 라면.
            charge += path[now][l]
            move(l, depth+1)   
            charge -= path[now][l] 
    visit[now] = 0 

n = int(sys.stdin.readline()) 
path = [list(map(int, sys.stdin.readline().split())) for _ in range(n)] 

visit = [0] * n 		#0혹은 false 값이 차있는 리스트 생성. 검증용/ 같은 행이 반복되지 않게끔.	

link = {}                #link는 딕셔너리형

charge, ans = 0, 10**7   #ans는 min함수를 이용하기위해 각 행렬의 최대값으로 미리 주어졋다.

for i in range(n): 		#딕셔너리 link에

    link[i] = []        #각 index i가 해당하는 곳에

    for j in range(n): 
        if path[i][j] > 0:    
            link[i].append(j)  #path에 저장되어있는 link
            
#print(link) = {0: [1, 2, 3], 1: [0, 2, 3], 2: [0, 1, 3], 3: [0, 1, 2]}
#path[i]의 i가 key, path[i][j] 중 0이 아닌 것들의 index 값이 저장됬다.
            
move(0, 1) 
print(ans)

    