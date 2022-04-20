# 2588


# 1. 세자리 두 자연수를 입력 받는다
# 2. 두번째 입력 받은 수의 세번째 자리와 첫번째 입력받은 수를 곱한다.
# 3. 2 과정을 두 번째 입력받은 수의 첫자리까지 반복하며 이를 출력한다.

a = input()
b = input()

ab2 = int(a)*int(b[2])
ab1 = int(a)*int(b[1])
ab0 = int(a)*int(b[0])
ab = int(a)*int(b)

print(ab2, ab1, ab0, ab, sep='\n')