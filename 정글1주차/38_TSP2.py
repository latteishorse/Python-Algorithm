# 완전 탐색 + N-queen 재귀
import sys 
global charge, ans 	

def move(now, depth):
    if depth == n:			  
        if now != 0:
            ans = min(ans, charge + path[now][0])
        return 
        
    visit[now] = 1		#현재/ now -> 이미 방문

    for l in link[now]:      #link[now] = path의 비용중 0이 아닌 것들의 인덱스
        if not visit[l]:     #visit[l]의 element가 false 라면.
            charge += path[now][l]
            move(l, depth+1)   
            charge -= path[now][l] 
    visit[now] = 0 

n = int(sys.stdin.readline()) 

path = [list(map(int, sys.stdin.readline().split())) for _ in range(n)] 

visit = [0] * n 	
link = {}             
charge, ans = 0, 10**7 

for i in range(n): 		
    link[i] = []       
    for j in range(n): 
        if path[i][j] > 0:    
            link[i].append(j)  #path에 저장되어있는 link
            
#print(link) = {0: [1, 2, 3], 1: [0, 2, 3], 2: [0, 1, 3], 3: [0, 1, 2]}
#path[i]의 i가 key, path[i][j] 중 0이 아닌 것들의 index 값이 저장됬다.
            
move(0, 1) 
print(ans)

    