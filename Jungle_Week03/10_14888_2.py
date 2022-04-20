from sys import stdin, maxsize
input = stdin.readline

N = int(input())
Arr = list(map(int, input().strip().split()))
operator = list(map(int, input().strip().split()))
mini = maxsize
maxi = -maxsize

def dfs(i,value):
    global mini, maxi
    if i == N-1:
        mini = min(mini,value)
        maxi = max(maxi,value)
    for j in range(4):
        if operator[j] > 0:
            operator[j] -= 1
            if j==0:
                dfs(i+1, value+Arr[i+1])
            elif j==1:
                dfs(i+1, value-Arr[i+1])
            elif j==2:
                dfs(i+1, value*Arr[i+1])
            elif j==3:
                dfs(i+1, int(value/Arr[i+1]))

                # if value < 0:
                #     dfs(i+1, -(-value//Arr[i+1]))
                # else:
                #     dfs(i+1, value//Arr[i+1])
            operator[j] += 1


dfs(0, Arr[0])
print(maxi)
print(mini)    