
# 덱으로
# 
# 리스트에 쭉 입력 받아서
#  index(max(list))

# import sys
# # from collections import deque
# input = sys.stdin.readline

# tc = int(input())

# n, m = map(int, input().split())
# doc = list(map(int,input().split()))

# # print(max(doc))
# # print(doc.index(max(doc)))

# # index 값을 찾았으니 해당 인덱스 앞 부분은 모두 팝해서 뒤로

# cnt = 1

# while doc :
#     if doc[m] != max(doc):
#         for i in range(doc.index(max(doc))):
#             doc.append(doc.pop(0))
#             cnt += 1
#         doc.pop(0)
    
#     elif doc[0] == max(doc):
#         for i in range(doc.index(max(doc))):
#             doc.append(doc.pop(0))
#             cnt += 1
#         break

#     else :
#         print('error')
#         break

# print(doc, cnt)
# -> 인덱스가 제대로 못따라감

# ---
# 현재 수의 위치를 따로 저장해줘야함

# https://assaeunji.github.io/python/2020-05-04-bj1966/

tc = int(input())

for _ in range(tc):
    n,m = list(map(int, input().split()))
    doc = list(map(int, input().split()))
    posDoc = list(range(len(doc)))
    posDoc[m] = "1"
    order = 0
    while doc:
        if doc[0]== max(doc):
            order += 1
            if posDoc[0]== "1":
                print(order)
                break
            else:
                doc.pop(0)
                posDoc.pop(0)
        else:
            doc.append(doc.pop(0))
            posDoc.append(posDoc.pop(0))        