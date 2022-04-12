# 4673

# 시작 한 수
# 
# 시작 수 + 각 자리 더함
# 그 값이 다음 수가 됨
# 반복

# 숫자를 만든다음에
# 전체 숫자에서 만들어진 숫자를 빼면 될듯

originNum = set(range(1, 10001))
genNum = set()    

for i in range(1, 10001):
    for j in str(i):
        i += int(j)
    genNum.add(i)

selfNum = sorted(originNum - genNum)
for i in selfNum:
    print(i)