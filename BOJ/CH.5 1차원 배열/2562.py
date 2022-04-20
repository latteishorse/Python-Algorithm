# 2562
# 9개의 서로 다른 자연수가 주어질 때, 이들 중 최댓값을 찾고 그 최댓값이 몇 번째 수인지를 구하는 프로그램을 작성하시오.
# 예를 들어, 서로 다른 9개의 자연수
# 3, 29, 38, 12, 57, 74, 40, 85, 61
# 이 주어지면, 이들 중 최댓값은 85이고, 이 값은 8번째 수이다.

# https://velog.io/@jsw8050/%EB%B0%B1%EC%A4%80-2562%EB%B2%88-1%EC%B0%A8%EC%9B%90-%EB%B0%B0%EC%97%B4-%EC%B5%9C%EB%8C%93%EA%B0%92-Python

num = []
for numbers in range(9):
    # append를 통해서 수 추가
    num.append(int(input()))
print(max(num))
print(num.index(max(num))+1)