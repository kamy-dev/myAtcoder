from typing import List

# Binary Searchの実装
def binary_search(A: List[int], key: int) -> int:
    left = 0
    right = len(A) - 1

    while left <= right:
        mid = (left + right) // 2
        if A[mid] == key:
            return mid
        elif A[mid] < key:
            left = mid + 1
        else:
            right = mid - 1
    return -1

if __name__ == "__main__":
    n = int(input())
    A = list(map(int, input().split()))
    q = int(input())
    B = list(map(int, input().split()))
    B.sort()

    ans = set()
    for key in A:
        if binary_search(B, key) != -1:
            ans.add(key)

    print(len(ans))
