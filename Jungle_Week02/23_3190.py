# # 3190
# from pprint import pprint

# n = int(input())

# # pprint
# li = [[(0,0) for x in range(n)] for y in range(n)]
# pprint(li)


# # apple
# k = int(input())
# apple = [list(map(int,input().split())) for _ in range(k)]

# # direction
# l = int(input())
# move = [list(map(int,input().split())) for _ in range(l)]

# # 현재 좌표
# nl = [1,1]

# # 초기시간 설정
# t = 0

# # --
# # 비운더리를 n으로 설정해주고 n 보다 클 경우 break
# while True :

#     if nl[0] > n or nl[1] > n :
#         break
    
#     # 이동하는 동안 초 증가
#     # 한칸 이동에 1초 증가

#     moveLocation = move[0]
#     for _ in range(l):
#         for j in range(int(move[j]+move[j+1])):

