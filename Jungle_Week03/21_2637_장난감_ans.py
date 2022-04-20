# https://firecatlibrary.tistory.com/26?category=862101

import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
 
need_parts = [[] for _ in range(N+1)]

parts_needed = [0]*(N+1)
EA_list = [0]*(N+1)
visited = [0]*(N+1)
basic = []
 
for m in range(M):
    x, y, EA = map(int,input().split())
    need_parts[x].append([y,EA])
    # 
    parts_needed[y] += 1


# print(need_parts, '1')
# print(parts_needed, '1')
 
while sum(parts_needed) > 0: # 필요한 부품 수
    for i in range(1,N+1):
        # print(EA_list, '횟수', i)
        if not need_parts[i] and visited[i] == 0:
            basic.append(i) # 1,2,3,4 append
            visited[i] = 1
            # print('basic tool', basic)
      
        if parts_needed[i] == 0 and visited[i] == 0:

            if EA_list[i] == 0:
                EA_list[i] = 1
            visited[i] = 1
 
            for j in need_parts[i]:
                EA_list[j[0]] += j[1]*EA_list[i]
                # 
                parts_needed[j[0]] -= 1
 
for i in basic:
    print(i, EA_list[i], sep=" ")
