# 2588

# 숫자형은 인덱싱할 수 없으므로
# 자료형으로 변환 후 원소 출력

a = str(input())
b = str(input())
b0 = b[2]
b1 = b[1]
b2 = b[0]
print(int(a) * int(b0), int(a) * int(b1), int(a) * int(b2), int(a) * int(b), sep='\n')

# -> 런타임 오류
#  배열이 할당된 크기를 넘어서
# index를 [-1]로 뒤에서 받아오면 오류 발생 

