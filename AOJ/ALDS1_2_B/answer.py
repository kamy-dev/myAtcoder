def selection_sort(A: list[int], n: int) -> None:
    cnt = 0
    for i in range(n):
        minj = i
        for j in range(i, n):
            if A[minj] > A[j]:
                minj = j 
        A[i], A[minj] = A[minj], A[i]
        if i != minj:
            cnt += 1   
    print(*A)
    print(cnt)

if __name__ == '__main__':
    n = int(input())
    A = [int(i) for i in input().split()]
    selection_sort(A, n)
