# 6549

# 가장 큰 직사각형은 분명 히스토그램의 적어도 하나의 막대의 윗부분과 붙어 있어야 한다.
# https://atgane.github.io/%EB%B0%B1%EC%A4%80/%EC%8A%A4%ED%83%9D/2021/02/10/%EB%B0%B1%EC%A4%80-6549-%ED%8C%8C%EC%9D%B4%EC%8D%AC.html

import sys
while True:
    input_list = list(map(int, sys.stdin.readline().split()))

    if input_list[0] == 0:
        break

    #
    input_list.append(0)

    ret = 0
    stack = [[0, 0]]

    for i in range(1, input_list[0] + 2):

        while stack[-1][1] > input_list[i]:
            tmp_list = stack.pop()
            tmp_area = 0

            while stack[-1][1] == tmp_list[1]:
                stack.pop()
            tmp_area = max((i - 1 - stack[-1][0]) * tmp_list[1], (i - tmp_list[0]) * tmp_list[1])

            if tmp_area > ret:
                ret = tmp_area
        stack.append([i, input_list[i]])

    print(ret)