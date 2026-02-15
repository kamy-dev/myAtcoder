def bubble_sort(A: list[int], n: int) -> None:
    flag = 1
    cnt = 0

    while flag:
        flag = 0
        for i in range(n-1, 0, -1):
            if A[i] < A[i-1]:
                A[i], A[i-1] = A[i-1], A[i]
                flag = 1
                cnt += 1
    print(*A)
    print(cnt)

if __name__ == '__main__':
    n = int(input())
    A = list(map(int, input().split()))
    bubble_sort(A, n)
