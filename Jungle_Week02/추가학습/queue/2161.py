# 17225

import sys
from collections import deque
input = sys.stdin.readline
n = int(input())

card = [i for i in range(1,n+1)]
dis_card = []

while len(card) != 1:
    dis_card.append(card.pop(0))
    card.append(card.pop(0))

for i in dis_card:
    print(i, end=' ')

print(card[0])