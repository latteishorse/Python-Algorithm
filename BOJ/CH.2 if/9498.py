# 9498
# 시험 점수를 입력받아 90 ~ 100점은 A, 80 ~ 89점은 B, 70 ~ 79점은 C, 60 ~ 69점은 D, 나머지 점수는 F를 출력하는 프로그램을 작성하시오.

A = input()
if int(A) > 89 :
    print('A')
elif int(A) > 79 :
    print('B')
elif int(A) > 69 :
    print('C')
elif int(A) > 59 :
    print('D')
else :
    print('F')