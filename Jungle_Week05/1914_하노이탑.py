# 중위순회
'''
def inorder(root):
    if root != '.':
        inorder(tree[root][0])  # left
        print(root, end='')  # root
        inorder(tree[root][1])  # right
'''

# 1914
def hanoi(n, rod1, rod3, rod2):
    if n == 1:
        print(rod1, rod3)
    elif n > 20:
        exit(0)
    else:
        hanoi(n-1, rod1, rod2, rod3)
        print(rod1, rod3)
        hanoi(n-1, rod2, rod3, rod1)

n = int(input())

print(2 ** n -1)
hanoi(n, 1,3,2)
