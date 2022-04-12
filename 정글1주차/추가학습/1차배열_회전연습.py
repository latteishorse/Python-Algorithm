# 1
# 슬라이싱
# arr = [1,2,3,4,5]
# print(arr[1:5] + arr[:1])
#을 응용하여

arr = [1,2,3,4,5]
n = int(input())

def rotate(arr, n):
    # 1.
    # if not arr:
    #     return arr
    n %= len(arr)
    # if not n:
    #     return arr
    # 2.
    left = arr[:-n]
    right = arr[-n:]

    # 3.
    return right + left
print(rotate(arr,n))


# 분할정복
def swap(arr, h, t, size):
    # 1.
    if h > t:
        swap(arr, t, h, size)
    # 2.
    if h + size > t:
        raise IndexError("Swap range is dupliacated")
    tmp = [None for _ in range(size)]

    for i in range(size):
        tmp[i] = arr[h+i]
        arr[h+i] = arr[t+i]
        arr[t+i] = tmp[i]        
    return

def rotate(arr, n):
    # 1. 
    if not arr:
        return arr
    N = len(arr)
    n %= N
    if not n:
        return arr

    def solve(lo, mid, hi):
        # 2.
        # lo는 왼쪽 구간의 첫 인덱스
        # mid는 왼쪽 구간의 마지막 인덱스
        # mid+1은 오른쪽 구간의 첫 인덱스
        # hi는 오른쪽 구간의 마지막 인덱스
        l_size = mid - lo + 1
        r_size = hi - mid

        # 3.
        if l_size == r_size:
            swap(arr, lo, mid+1, l_size)
            return

	# 4.
        if l_size > r_size:
            swap(arr, lo, mid+1, r_size)
            solve(lo+r_size, mid, hi)
        else:
            swap(arr, lo, hi-l_size+1, l_size)
            solve(lo, mid, hi-l_size)
    
    # 5.
    solve(0, N-n-1, N-1)
    return arr

print(rotate(arr,n))
