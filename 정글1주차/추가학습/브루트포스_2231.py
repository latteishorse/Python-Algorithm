# originNum = set(range(1, 10001))
# genNum = set()    

# for i in range(1, 10001):
#     for j in str(i):
#         i += int(j)
#     genNum.add(i)

# selfNum = sorted(originNum - genNum)
# for i in selfNum:
#     print(i)

# ---
n = int(input())

for i in range(1, n+1):
    num = sum((map(int, str(i)))) #-> 각자리 수를 더함

    num_sum = i + num # 생성자 + 각자리 수 합
    if num_sum == n:
        print(i)
        break

    if i == n: # -> 입력값과 같다 = 생성자가 없다
        print(0)