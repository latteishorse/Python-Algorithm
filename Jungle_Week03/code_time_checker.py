import time
start_time = time.time()
# ------


# ------
end_time = time.time()
print("time :", end_time - start_time)

# ## ---
# import sys
# import heapq
# input = sys.stdin.readline
 
# V, E = map(int, input().split())
# # -
# start_time = time.time()
# # - 

# visited = [False]*(V+1)
# Elist = [[] for _ in range(V+1)]
# heap = [[0, 1]]
# for _ in range(E):
#     s, e, w = map(int, input().split())
#     Elist[s].append([w, e])
#     Elist[e].append([w, s])
 
# answer = 0
# cnt = 0
# while heap:
#     if cnt == V:
#         break
#     w, s = heapq.heappop(heap)
#     if not visited[s]:
#         visited[s] = True
#         answer += w
#         cnt += 1
#         for i in Elist[s]:
#             heapq.heappush(heap, i)
 
# print(answer)

# end_time = time.time()
# print("prim algo. time :", end_time - start_time)

# ------
# # 2. Kruskal
# import sys
# input = sys.stdin.readline
 
# V, E = map(int, input().split())
# # -
# start_time = time.time()
# # - 

# Vroot = [i for i in range(V+1)]
# Elist = []
# for _ in range(E):
#     Elist.append(list(map(int, input().split())))
 
# Elist.sort(key=lambda x: x[2])
 
 
# def find(x):
#     if x != Vroot[x]:
#         Vroot[x] = find(Vroot[x])
#     return Vroot[x]
 
 
# answer = 0
# for s, e, w in Elist:
#     sRoot = find(s)
#     eRoot = find(e)
#     if sRoot != eRoot:
#         if sRoot > eRoot:
#             Vroot[sRoot] = eRoot
#         else:
#             Vroot[eRoot] = sRoot
#         answer += w
 
# print(answer)

# end_time = time.time()
# print("kruskal algo. time :", end_time - start_time)
