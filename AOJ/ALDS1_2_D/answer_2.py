def bubble_sort(A: list[int], n: int, g: int) -> int:
    cnt=0
    for i in range(g, n):
        v = A[i]    # ここでA[i]の値をメモリに保持しておく。
        j = i - g
        while j >= 0 and A[j] > v:
            A[j+g] = A[j]
            j = j - g
            cnt += 1
        A[j+g] = v
    return cnt

def shell_sort(A: list[int], n: int) -> None:
    g = []
    h = 1
    while h <= n:
        g.append(h)
        h = 3*h+1
    g.reverse()
    m = len(g)
    print(m)
    print(' '.join(map(str, g)))
    cnt = 0
    for i in range(m):
        cnt += bubble_sort(A, n, g[i])
    print(cnt)
    print('\n'.join(map(str, A)))

if __name__ == '__main__':
    n = int(input())
    A = [int(input()) for _ in range(n)]
    shell_sort(A,n)
