from itertools import permutations
n = int(input())
k = int(input())
numbers = [input() for _ in range(n)]

ans = set()
for i in permutations(numbers, k):
    ans.add(''.join(i))

print(len(ans))