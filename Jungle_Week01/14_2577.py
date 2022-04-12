# 2577
# 숫자의 개수

# a = int(input())
# b = int(input())
# c = int(input())

# num = list(str(a * b * c))
# answer = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

# # string 값으로 왼쪽부터 하나씩
# # 
# for i in num:
#     answer[int(i)] += 1

# # 
# print(answer)
# for j in answer:
#     print(j)

# print(num, "2")

# # ['7','9','8','6']
# for num in answer:
#     print(num)

# print(num, "3")

#  --------

a = int(input())
b = int(input())
c = int(input())
num = list(str(a * b * c))
ans = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
for i in num:
    ans[int(i)] += 1
for j in ans:
    print(j)