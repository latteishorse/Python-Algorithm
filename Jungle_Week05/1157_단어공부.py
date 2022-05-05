# 1157
# 알파벳 대소문자로 된 단어가 주어지면, 이 단어에서 가장 많이 사용된 알파벳이 무엇인지 알아내는 프로그램을 작성하시오. 단, 대문자와 소문자를 구분하지 않는다.
import sys
input = sys.stdin.readline

word = map(ord,input().strip().upper())
wordList = [0] * 128

for i in word:
    wordList[i] += 1

maxWord = 0
for j in wordList:
    maxWord = max(j, maxWord)

if wordList.count(maxWord) > 1:
    print('?')
    exit(0)

print(chr(wordList.index(maxWord)))
