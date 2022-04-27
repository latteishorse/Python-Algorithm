# 9249
# Longest Common Substring
# 메모리 초과
# 정답 출력

firstWord = input().strip()
secondWord = input().strip()

firstWordLength = len(firstWord)
secondWordLength = len(secondWord)

# 2차 배열 -> 10만 * 10만으로 메모리 초과
LCS = [[0] * (secondWordLength+1) for _ in range(firstWordLength+1)]

# 2차 배열 메모리 만족하더라도 시간 복잡도 O(N^2)으로 시간 초과
maxLCS = 0
for i in range(1, firstWordLength+1):
    for j in range(1, secondWordLength+1):
        if firstWord[i-1] == secondWord[j-1]:
            LCS[i][j] = LCS[i - 1][j - 1] + 1
        else:
            LCS[i][j] = 0

        maxLCS = max(LCS[i][j], maxLCS) 
        if LCS[i][j] == maxLCS:
            maxIndex = [i,j]
   
print(maxLCS)

word = list(firstWord) 
# print(''.join(word[maxIndex[0] - maxLCS : maxIndex[0]]))
print(*word[maxIndex[0] - maxLCS : maxIndex[0]], sep = '')
