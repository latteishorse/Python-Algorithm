# 2577

# 중복을 카운트


num1 = int(input())
num2 = int(input())
num3 = int(input())

count_num = list(str(num1 * num2 * num3))

answer = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for i in count_num:
    answer[int(i)] += 1

for ans in answer:
    print(ans)