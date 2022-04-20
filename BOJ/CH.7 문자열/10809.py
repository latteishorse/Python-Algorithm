# 10809
# 220318

# 알파벳 소문자로만 이루어진 단어 S가 주어진다. 각각의 알파벳에 대해서, 단어에 포함되어 있는 경우에는 처음 등장하는 위치를, 포함되어 있지 않은 경우에는 -1을 출력하는 프로그램을 작성하시오.

# 각각을 카운트 해야됨
# 단어 검색 유사도 문제랑 비슷?
# https://youtu.be/BF3FLDAzWxo

# def isAnagram(a, b):
#    return sorted(a) == sorted(b)

word = input()
alphabet = list(range(97,123))

for x in alphabet :
    print(word.find(chr(x))) 
