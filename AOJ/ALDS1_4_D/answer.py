def can_load(P: int, l: list, k: int) -> bool:
    """
    最大積載量Pで、荷物リストlをk台以下のトラックに積めるかを判定する。
    荷物は順番通りに連続して積む必要がある。
    
    Args:
        P: トラック1台あたりの最大積載量
        l: 荷物の重さのリスト
        k: トラックの台数
    
    Returns:
        True: k台以下で全て積める
        False: k台では足りない

    """
    truck = 1
    total = 0
    for weight in l:
        if total + weight <= P:
            total += weight
        else:
            truck += 1
            total = weight
    return truck <= k

def binary_search(l: list, k: int):
    """
    全ての荷物をk台のトラックに積むために必要な最大積載量Pの最小値を
    二分探索で求める。

    Args:
        l: 荷物の重さのリスト
        k: トラックの台数

    Returns:
        最大積載量Pの最小値
    """
    left = max(l)
    right = sum(l)

    while left < right:
        P = (left + right) // 2
        if can_load(P, l, k):
            # もっと最大積載量Pを小さくできる
            right = P
        else:
            # もっと最大積載量Pを大きくできる
            left = P + 1
    return left

n, k = input().split()
n = int(n)
k = int(k)
l = [int(input()) for _ in range(n)]

print(binary_search(l, k))

