# 5639

import sys
input = sys.stdin.readline
# 재귀 깊이 제한
sys.setrecursionlimit(10 ** 6)
# root

# node 값들이 순차적으로 입력됨
# 입력된 값은 전위 순회한 결과 값

# 전위 순회 -> 이진 트리 -> 후위 순회

# 이진 탐색 -> 정렬되어 있음
# -> 정렬이 깨지는 시점까지 레벨이 내려가면 됨

def postorder(start, end):
    # while start < end:
    if start > end:
        return
    else:
        # preorder 중 하나 임의 선택
        root = preorder[start]

# mid를 end + 1로 초기화하는 이유
# 만약 모든 원소가 루트 노드보다 작은 경우
# post(start + 1, mid - 1) : start + 1, # end 가 삽입, 즉 루트 노드를 제외한 트리

# post(mid, end) : end + 1, end 가 삽입되어 if start > end: return에 의해 리턴됨 이는 오른쪽 노드가 없음을 의미

        mid = end + 1

        for i in range(start + 1, end + 1):
            if root < preorder[i]:
                mid = i
                break

# 후위 탐색
        # 루트 노드보다 작은 원소
        postorder(start+1, mid-1) # 왼쪽 트리

        # 루트 노드보다 큰 원소
        postorder(mid, end) # 오른쪽 트리
        print(root) # 루트 노드

preorder = []
# 노드 값만 주어짐
while True:
    try:
        preorder.append(int(input()))
    # EOF 처리는 except로
    except:
        break

postorder(0, len(preorder)-1)
