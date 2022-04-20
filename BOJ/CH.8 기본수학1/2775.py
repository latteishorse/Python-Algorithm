# 2775

# 1 2 3 4 ... i
# test case
# k
# n
# 1층 3호 
# 2층 3호

# a층 b호에 살려면 a-1층의 1호부터 b호까지 사람의 합을 데려와야한다

# 1층 1호
# 0층 1호 >

# 1층 2호
# 0층, 1호, 2호

# 2층 : 1 4 10 20
# 1층 : 1 3 6 10
# 0층 : 1 2 3 4

T = int(input())

for i in range (T):
    k = int(input())
    n = int(input())
    people = [i for i in range(1, n+1)]

    #[1, 2, 3, 4, 5]
    for _ in range(k):
     for j in range(1, n):
         people[j] += people[j-1]
    # for x in range(k):
    print(people[-1])