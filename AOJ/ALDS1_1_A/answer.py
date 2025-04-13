import sys

def main():
    n = int(input())
    A = [int(i) for i in input().split()]
    print(f'nの参照カウント: {sys.getrefcount(n)}')
    print(f'Aの参照カウント: {sys.getrefcount(A)}')
    print(f'nのサイズ(byte): {sys.getsizeof(n)}')
    print(f'Aのサイズ(byte): {sys.getsizeof(A)}')

    for i in range(n):
        v = A[i]
        j = i-1
        while j>=0 and A[j] > v:
            A[j+1] = A[j]
            j -= 1
        A[j+1] = v
        print(*A)
    return

if __name__ == '__main__':
    main()