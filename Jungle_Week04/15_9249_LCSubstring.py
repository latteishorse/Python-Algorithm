# 9249
# Longest Common Substring
# 메모리 초과

firstWord = input().strip()
secondWord = input().strip()

firstWordLength = len(firstWord)
secondWordLength = len(secondWord)

LCS = [[0] * (secondWordLength+1) for _ in range(firstWordLength+1)]

maxLCS = 0
for i in range(1, firstWordLength+1):
    for j in range(1, secondWordLength+1):
        if firstWord[i-1] == secondWord[j-1]:
            LCS[i][j] = LCS[i - 1][j - 1] + 1
        else:
            LCS[i][j] = 0

        maxLCS = max(LCS[i][j], maxLCS) # 이 부분에서 완전탐색 한번더 하는게 문제?
        if LCS[i][j] == maxLCS:
            maxIndex = [i,j]
   
print(maxLCS)

word = list(firstWord) # 이 부분도 문제?
# print(''.join(word[maxIndex[0] - maxLCS : maxIndex[0]]))
print(*word[maxIndex[0] - maxLCS : maxIndex[0]], sep = '')

