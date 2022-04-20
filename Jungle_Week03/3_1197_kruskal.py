# 1197
# kruskal algo.

# 2. Kruskal
import sys
input = sys.stdin.readline
 
# vertex, edge
V, E = map(int, input().split())

# root를 저장하는 배열 Vroot
Vroot = [i for i in range(V+1)]

# edge를 가중치 순으로 오름차순 정렬
Elist = []
for _ in range(E):
    Elist.append(list(map(int, input().split())))
 
Elist.sort(key=lambda x: x[2])

def find(x):
    if x != Vroot[x]:
        Vroot[x] = find(Vroot[x])
    return Vroot[x]
 
 
answer = 0
for s, e, w in Elist:
    sRoot = find(s)
    eRoot = find(e)

# 가중치를 더한다
# union
    if sRoot != eRoot:
        if sRoot > eRoot:
            Vroot[sRoot] = eRoot
        else:
            Vroot[eRoot] = sRoot
        answer += w
 
print(answer)