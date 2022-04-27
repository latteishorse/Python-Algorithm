# 2487

# N개의 레벨
# 쉬운 레벨이 어려운 레벨보다 점수를 많이 받는 경우

# -> 해결을 위해 특정 레벨의 점수를 감소 시키고자 함
# 

# 레벨의 수 N
n = int(input())
nums = []
for _ in range(n):
    nums.append(int(input()))
# nums.sort()
cnt = 0
# while nums[0] >= nums[1]:
for i in range(n-1, 0, -1):
    if nums[i-1] >= nums[i]:
        cnt += (nums[i-1] - nums[i]) + 1
        nums[i-1] = nums[i] - 1
print(cnt)