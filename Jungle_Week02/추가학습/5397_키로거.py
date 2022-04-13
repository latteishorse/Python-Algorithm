# 5397

# 입력한 순서대로 길이 l 문자열
# 벡스페이스 '-' : 커서 앞에 글자가 있었으면 지운다
# 화살표 입력 '<' , '>' : 왼쪽 또는 오른쪽으로 1만큼 움직
# 
import sys
input = sys.stdin.readline

tc = int(input())
for _ in range(tc):
    pw = str(input()) 
    stack = []
    temp = []

    for i in pw:
        if i == '-':
            if stack:
                stack.pop()
        
        elif i == '>':
            if temp:
                stack.append(temp.pop())

        elif i == '<':
            if stack:
                temp.append(stack.pop())

        else:
            stack.append(i)

    temp.reverse()
    print(''.join(stack), end='')
    print(''.join(temp))