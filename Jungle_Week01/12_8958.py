# 8958
# ox 퀴즈 - 문자열

# 전 문자가 o면 score에 + 1을 누적
# 전 문자가 무엇인지 판단하여 1점을 줄지, 누적된 점수에 + 1을 해서 줄지 결정


# 초기 풀이 컨셉

# num = int(input())
# score = 0

# for k in range (num):
#     test = list(str(input()))

# # range 값을 len으로 받는 것은 파이썬에서 비권장하는 패턴
# for i in range (0, len(test)):
#     if test[i] == "O":
#         score += 1

# print(score)

# -------------------

# string 값은 array 가능

N = int(input())
for i in range(N):
    score = 0
    sumScore = 0
    a = input()
    for j in a:
        if j == 'O':
            score += 1
        else:
            score = 0
        sumScore += score
    print(sumScore)