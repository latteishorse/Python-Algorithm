# 9084, 3067
# 동전으로 금액을 만드는 모든 경우의 수

# DP
# 배낭문제
# 금액 범위 (1<= <=10000) 

# 테스트 케이스 T
# 동전의 가지 수 N
# N가지 동전의 각 금액
# 만들어야 할 금액 M

# - 문제 분석
# 코인 * 특정 수 + 코인 * 특정 수 = 목표 금액
# n개의 코인을 사용해서 완성했을 때
# n번 인덱스에 체크

# 코인의 재귀식을 구해야 하나?
# 모든 경우의 수를 판단할 수 없으니 일반화 해야할듯?

t = int(input())
for i in range(t):
    n = int(input())
    c = list(map(int, input().split()))
    m = int(input())

    dp = [0 for i in range(m + 1)]

    dp[0] = 1
    for i in c:
        for j in range(1, m + 1):
            # if j - i >= 0: # 232ms
            if j >= i: # 188ms

                dp[j] += dp[j - i]
    print(dp[m])


'''
구하려는 값에서 현재까지 코인으로 만든 값을 빼고
뺀 값에서 남은 코인으로 만든 값을 빼고
이걸 반복하면 되지 않을까

예를 들어
첫 번째 코인 500개를 썼으면
500개 쓴 경우를 저장해두고, 다음 499개 쓴 경우를 판단
이런 식으로 코드가 작동하면 어떨까?


'''

# -> 그리디 처럼 접근하면 안됨
# temp = [False] * 10
# temp = []

# cnt = 0
# for i in coin:
#     # if not temp:
#         if M % i == 0:
#             cnt = M // i
#             temp.append(cnt)

#         else:
#             print('else')

#     # print(i)
#     # cnt += 1


# print(*temp)