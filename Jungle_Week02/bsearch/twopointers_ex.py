# two pointers

# 특정합을 가지는 부분 연속 수열

# 데이터의 개수 N, 부분 연속 수열의 합 M
n, m = 5, 5
data = [1,2,3,2,5]

result = 0
summary = 0
end = 0

# start를 차례대로 증가
for start in range(n):
    while summary < m and end < n :
        summary += data[end]
        end += 1
    
    if summary == m:
        result += 1
    summary -= data[start]

print(result)

