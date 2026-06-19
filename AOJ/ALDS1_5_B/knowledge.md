# Review memo

## マージソート

https://onlinejudge.u-aizu.ac.jp/courses/lesson/1/ALDS1/5/ALDS1_5_B

## マージソートとは
- 分割統治法に基づく高速なアルゴリズム。コードにすると以下

```python
INFTY = float('inf')   # 番兵として使う「無限大」

def merge(A, left, mid, right):
    n1 = mid - left
    n2 = right - mid
    
    # 左半分・右半分をコピー（末尾に INFTY を番兵として追加）
    L = [A[left + i]  for i in range(n1)] + [INFTY]
    R = [A[mid  + i]  for i in range(n2)] + [INFTY]
    
    i = 0
    j = 0
    for k in range(left, right):
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1


def mergeSort(A, left, right):
    if left + 1 < right:
        mid = (left + right) // 2
        mergeSort(A, left, mid)
        mergeSort(A, mid, right)
        merge(A, left, mid, right)


# 動作確認
A = [5, 2, 4, 7, 1, 3, 2, 6]
mergeSort(A, 0, len(A))
print(A)   # [1, 2, 2, 3, 4, 5, 6, 7]
```

