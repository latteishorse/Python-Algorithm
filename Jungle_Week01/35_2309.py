# 2309
# continue, exit

# n = 9
# arr = []
# for _ in range(n):
#     arr.append(int(input()))
# arr.sort()

# for i in range(n):
#     for j in range(i+1, n):

#         if sum(arr) - (arr[i] + arr[j]) == 100:

#             for k in range(9):
#                 if i == k or j == k:

#                     continue

#                 print(arr[k])
#             exit()
 
# print('\n'.join(map(str, arr)))

# ----
# temp, remove
 
# n = 9
# temp1, temp2 = 0, 0
# arr = [int(input()) for _ in range(n)]
 
# for i in range(n):
#     for j in range(i+1, n):
#         if sum(arr) - (arr[i] + arr[j]) == 100:
#             temp1 = arr[i]
#             temp2 = arr[j]
 
# arr.remove(temp1)
# arr.remove(temp2)
 
# print('\n'.join(map(str, sorted(arr))))

# ---
n = 9
t1, t2 = 0, 0
b = []
for i in range(n):
    b.append(int(input()))
for i in range(n):
    for j in range(i+1, n):
        if sum(b) - b[i] - b[j] == 100:
            t1 = b[i]
            t2 = b[j]
b.remove(t1)
b.remove(t2)
b.sort()
print('\n'.join(map(str, b)))