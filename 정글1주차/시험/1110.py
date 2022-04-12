# import sys
# input = sys.stdin.readline

# def cycle(N):
#     global counter
#     if N < 10:
#         N= str(N)
#         n=  str()+ int(N[0])
#         counter += 1
#         cycle(n)

#     elif N > 9 and N < 100:
#         N= str(N)
#         n= int(N[-1:])*10 + (int(N[0])+int(N[1]))
#         counter += 1
#         if n == N:
#             return counter
#         cycle(n)
        
# N = int(input())
# counter = 0            
# cycle(N)
# print(counter)

# -----
# 몫, 나머지를 이용한 풀이

n = int(input())
count = 0
num = n

while True :
    a = num // 10
    b = num % 10
    c = (a+b) % 10
    num = (b * 10) + c
    count += 1
    
    if num == n:
        print(count)
        break
        