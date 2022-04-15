# 9935
import sys
input = sys.stdin.readline

word = input().strip()
bomb = input().strip()

stack = []

for i in word:
    if i != bomb[-1]:
        stack.append(i)

    else:
        stack.append(i)
        if ''.join(stack[-len(bomb):]) == bomb:
            for _ in range(len(bomb)):
                stack.pop()

if len(stack) == 0:
    print('FRULA')

else:
    print(''.join(map(str,stack)))
    