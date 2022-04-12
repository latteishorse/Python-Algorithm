# # 10989
# sorted

# https://pacific-ocean.tistory.com/67
# https://yoonsang-it.tistory.com/49


# n = int(input())
# x = [None] * n

# for i in range(n):
#     x[i] = int(input())

# x = sorted(x)
# for i in range(n):
#     print(x[i])

# #  -----
# #  퀵정렬

# from typing import MutableSequence

# def sort3(a: MutableSequence, idx1: int, idx2: int, idx3: int):
#     if a[idx2] < a[idx1]: a[idx2], a[idx1] = a[idx1], a[idx2]
#     if a[idx3] < a[idx2]: a[idx3], a[idx2] = a[idx2], a[idx3]
#     if a[idx2] < a[idx1]: a[idx2], a[idx1] = a[idx1], a[idx2]
#     return idx2

# def insertion_sort(a: MutableSequence, left: int, right: int) -> None:
#     for i in range(left + 1, right + 1):
#         j = i
#         tmp = a[i]
#         while j > 0 and a[j - 1] > tmp:
#             a[j] = a[j - 1]
#             j -= 1
#         a[j] = tmp

# def qsort(a: MutableSequence, left: int, right: int) -> None:
#     if right - left < 9:           
#         insertion_sort(a, left, right)
#     else:                           
#         pl = left                   
#         pr = right                 
#         m = sort3(a, pl, (pl + pr) // 2, pr)
#         x = a[m]

#         a[m], a[pr - 1] = a[pr - 1], a[m]
#         pl += 1
#         pr -= 2
#         while pl <= pr:
#             while a[pl] < x: pl += 1
#             while a[pr] > x: pr -= 1
#             if pl <= pr:
#                 a[pl], a[pr] = a[pr], a[pl]
#                 pl += 1
#                 pr -= 1

#         if left < pr: qsort(a, left, pr)
#         if pl < right: qsort(a, pl, right)

# def quick_sort(a: MutableSequence) -> None:
#     qsort(a, 0, len(a) - 1)

# if __name__ == '__main__':
#     num = int(input())
#     x = [None] * num   
#     for i in range(num):
#         x[i] = int(input())
#     quick_sort(x)
#     for i in range(num):
#         print(x[i])

#  정렬3
#  -> input으로 받으면 메모리 초과

#-----------
# 인덱싱을 이용한 정렬

import sys

n = int(sys.stdin.readline())
b = [0] * 10001

# 해당 리스트에 1 저장
# 값에 해당하는 위치에 1을 저장
for i in range(n):
    b[int(sys.stdin.readline())] += 1

# 해당 인덱스에 1이 저장되어 있으면 출력
for i in range(10001):
    if b[i] != 0:
        for _ in range(b[i]):
            print(i)

# 10개 정렬
# 0.00316초

# -------------


# import sys
# N = int(input())
# cnt_list = [0] * 10001

# for i in range(N):
#     cnt_list[int(input())] += 1

# for i in range(10001):
#     sys.stdout.write('%s\n' % i * cnt_list[i])

# 10개 정렬
# 0.01초
