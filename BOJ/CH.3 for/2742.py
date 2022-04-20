# 2742
# 자연수 N이 주어졌을 때, N부터 1까지 한 줄에 하나씩 출력하는 프로그램을 작성하시오.

a = int(input())

for i in range (1, a+1):
    i = a - i
    print(i+1)

# n=int(input())
# print("\n".join(map(str, range(n, 0, -1))))