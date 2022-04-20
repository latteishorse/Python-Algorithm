# 1712

# a + b * n대 > c * n대
# for i in range로
# 위 부등식이 처음으로 넘을 때 i를 출력하는 코드

# a, b, c = map(int, input().split())

# for i in range(1, ):
#     if (a+b*i) > (c*i):
#         i += 1
#     elif  (a+b*i) < (c*i):
#         print(i)
#     else :
#         print('-1')

a, b, c = map(int, input().split())
if b>= c:
    print(-1)
else :
    print(int(a/(c-b)+1))