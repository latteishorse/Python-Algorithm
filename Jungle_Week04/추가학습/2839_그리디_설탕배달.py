# 2839
# 정확하게 N키로 배달

# 설탕 3, 5키로
# 최대한 적게 가져가는 문제

# 5로 먼저 나누고
# 3으로 나누면 최소

# w = int(input())

# cnt = 0
# while w != 0:
#     if w // 5 != 0 and w % 5 == 3:
#         cnt = cnt + w // 5
#         w = w % 5
#     elif w // 3 != 0 :
#         cnt = cnt + w //3
#         w = w % 3


#     else:
#         break 
    
# if w == 0:
#     print(cnt)

# else :
#     print(-1)

# --
n=int(input())
cnt=0
while True:
    if n%5==0:
        print(cnt+n//5)
        break
    n-=3
    cnt+=1

    if n==0:
        print(cnt)
        break
    if n<0:
        print(-1)
        break