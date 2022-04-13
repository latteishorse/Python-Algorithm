# # 1417

# # 후보수는 n명
# # 마을 주민 m명

# # 예 
# # 1-5, 2-7, 3-7
# #  2번 -2, 3번 -1
# #하면 1번 후보가 당선

# n = int(input())
# peo = [list(map(int, input().split())) for _ in range(n)]
# cnt = 0

# while True:
#     cnt += 1
#     if n == 1:
#         cnt = 0
#         break

#     # 1번 후보다 제일 많을 때 루프 종료
#     if peo[0][0] > peo[1][0] and peo[0][0] > peo[2][0]:
#         break

#     # 케이스 1
#     # 1번 후보 보다 2, 3번 후보 중 한명이라도 많은 경우
#     # 해당 후보에서 하나씩 팝 시켜봄
#     # 팝 시킨 횟수를 cnt 에 저장

#     elif peo[0][0] <= peo[1][0]:
#         peo[1][0] -= 1
#         peo[0][0] += 1
#         # cnt += 1

#     elif peo[0][0] <= peo[2][0]:
#         peo[2][0] -= 1
#         peo[0][0] += 1
#         # cnt += 1

# print(cnt-1)

# ---

N=int(input())
ls=[]

for i in range(N):
    ls.append(int(input()))

dasom = ls[0]
rev = ls[1:N]

if N == 1:
    print(0)

else:
    num=0
    rev= sorted(rev,reverse=True)
    while rev[0]>=dasom:
        dasom+=1
        rev[0]-=1
        num+=1
        rev = sorted(rev,reverse=True)
    print(num)