# 1181
'''
알파벳 소문자로 이루어진 N개의 단어가 들어오면 아래와 같은 조건에 따라 정렬하는 프로그램을 작성하시오.

길이가 짧은 것부터
길이가 같으면 사전 순으로
'''

import sys ; input = sys.stdin.readline
n = int(input())
word = []
[word.append(input().strip()) for i in range (n)]
    
word = list(set(word))
word.sort()
word.sort(key = lambda x : len(x))

print("\n".join(word))