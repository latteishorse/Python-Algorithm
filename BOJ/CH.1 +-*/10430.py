# 10430
# (A+B)%C는 ((A%C) + (B%C))%C 와 같을까
# (A×B)%C는 ((A%C) × (B%C))%C 와 같을까?
# 세 수 A, B, C가 주어졌을 때, 위의 네 가지 값을 구하는 프로그램을 작성하시오.

# 첫째 줄에 (A+B)%C, 둘째 줄에 ((A%C) + (B%C))%C, 셋째 줄에 (A×B)%C, 넷째 줄에 ((A%C) × (B%C))%C를 출력한다.

# A,B,C = input().split()
# print((int(A)+int(B))%int(C))
# print((int(A)%int(B)+(int(B)%int(C)))%int(C))
# print((int(A)*int(B))%int(C))
# print((int(A)%int(B)*(int(B)%int(C)))%int(C))

a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)

print((a+b)%c)
print(((a%c)+(b%c))%c)
print((a*b)%c)
print(((a%c)*(b%c))%c)